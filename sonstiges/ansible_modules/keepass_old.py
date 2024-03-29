#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author:  Linuxfabrik GmbH, Zurich, Switzerland
# Contact: info (at) linuxfabrik (dot) ch
#          https://www.linuxfabrik.ch/
# License: The Unlicense, see LICENSE file.

# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: keepass

short_description: This a module to interact with a keepass (kdbx) database.

version_added: "2.7"

description:
    - "This a module to interact with a keepass (kdbx) database."

requirements:
    - PyKeePass

options:
    database:
        description:
            - Path of the keepass database.
        required: true
        type: str

    hostname:
        description:
            - Hostname, will be used for the title of the entry. Leave this blank for host-independent entries.
        required: false
        type: str

    keyfile:
        description:
            - Path of the keepass keyfile. Either this or 'password' (or both) are required.
        required: false
        type: str

    purpose:
        description:
            - Purpose, will be used for the title of the entry.
        required: true
        type: str

    username:
        description:
            - Username of the entry.
        required: true
        type: str

    password:
        description:
            - Path of the keepass keyfile. Either this or 'keyfile' (or both) are required.
        required: false
        type: str

    password_length:
        description:
            - The length of the generated passwords. Defaults to 30 characters.
        required: false
        type: int

author:
    - Linuxfabrik GmbH, Zurich, Switzerland, https://www.linuxfabrik.ch
'''

EXAMPLES = '''
- name: Create a new password, or get the existing item
  keepass:
    database: /tmp/vault.kdbx
    hostname: dbhost01.localdomain
    keyfile: /tmp/vault.key
    purpose: MariaDB
    username: mariadb-admin
  register: creds
- debug:
    msg: "Username: {{ creds.username }}, Password: {{ creds.password }}, New password: {{ creds.changed }}"

- name: Create a longer new password, or get the existing item
  keepass:
    database: /tmp/vault.kdbx
    hostname: "{{ inventory_hostname }}"
    keyfile: /tmp/vault.key
    password_length: 45
    purpose: MariaDB
    username: mariadb-admin
  register: creds
- debug:
    msg: "Username: {{ creds.username }}, Password: {{ creds.password }}, New password: {{ creds.changed }}"

- name: Create a new, host-independent password, or get the existing item
  keepass:
    database: /tmp/vault.kdbx
    keyfile: /tmp/vault.key
    password_length: 45
    purpose: MariaDB
    username: mariadb-admin
  register: creds
- debug:
    msg: "Username: {{ creds.username }}, Password: {{ creds.password }}, New password: {{ creds.changed }}"
'''

RETURN = '''
username:
    description: The original username that was passed in
    type: str
password:
    description: The generated or retrieved password
    type: str
'''
import traceback

from ansible.module_utils.basic import AnsibleModule,missing_required_lib

PYKEEPASS_IMP_ERR = None
try:
    from pykeepass import PyKeePass
    import pykeepass.exceptions
except ImportError:
    PYKEEPASS_IMP_ERR = traceback.format_exc()
    pykeepass_found = False
else:
    pykeepass_found = True

import subprocess
import argparse

def main():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        database=dict(type='str', required=True),
        hostname=dict(type='str', required=False),
        keyfile=dict(type='str', required=False, default=None),
        password=dict(type='str', required=False, default=None, no_log=True),
        password_length=dict(type='int', required=False, default=30, no_log=False),
        purpose=dict(type='str', required=True),
        username=dict(type='str', required=True),
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # change is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
        username='',
        password=''
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if not pykeepass_found:
        module.fail_json(msg=missing_required_lib("pykeepass"), exception=PYKEEPASS_IMP_ERR)

    database        = module.params['database']
    hostname        = module.params['hostname']
    keyfile         = module.params['keyfile']
    password        = module.params['password']
    password_length = module.params['password_length']
    purpose         = module.params['purpose']
    username        = module.params['username']

    if not password and not keyfile:
        module.fail_json(msg="Either 'password' or 'keyfile' (or both) are required.")

    try:
        kp = PyKeePass(database, password=password, keyfile=keyfile)
    except IOError as e:
        KEEPASS_OPEN_ERR = traceback.format_exc()
        module.fail_json(msg='Could not open the database or keyfile.')
    except CredentialsIntegrityError as e:
        KEEPASS_OPEN_ERR = traceback.format_exc()
        module.fail_json(msg='Could not open the database. Credentials are wrong or integrity check failed')

    # try to get the entry from the database
    entry = get_password(module, kp, hostname, username, purpose)
    if entry:
        entry_username, entry_password = entry
        if entry_username == username:
            result['username'] = entry_username
            result['password'] = entry_password
            module.exit_json(**result)

    # if there is no matching entry, create a new one
    password = generate_password(module, password_length)
    if not module.check_mode:
        try:
            set_password(module, kp, hostname, username, purpose, password)
        except:
            KEEPASS_SAVE_ERR = traceback.format_exc()
            module.fail_json(msg='Could not add the entry or save the database.', exception=KEEPASS_SAVE_ERR)

    result['username'] = username
    result['password'] = password
    result['changed'] = True

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)


def generate_password(module, length):
    import string
    alphabet = string.ascii_letters + string.digits
    try:
        import secrets as random
    except ImportError:
        import random

    password = ''.join(random.choice(alphabet) for i in range(length))
    return password


def set_password(module, kp, hostname, username, purpose, password):
    if hostname:
        kp.add_entry(kp.root_group, hostname + ' - ' + purpose, username, password, icon='47', notes='Generated by ansible.')
    else:
        kp.add_entry(kp.root_group, purpose, username, password, icon='47', notes='Generated by ansible.')

    kp.save()


def get_password(module, kp, hostname, username, purpose):
    if hostname:
        entry = kp.find_entries(title=hostname + ' - ' + purpose, first=True)
    else:
        entry = kp.find_entries(title=purpose, first=True)

    if (entry):
        return (entry.username, entry.password)
    else:
        return None


if __name__ == '__main__':
    main()
