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

    keyfile:
        description:
            - Path of the keepass keyfile. Either this or 'password' (or both) are required.
        required: false
        type: str

    title:
        description:
            - title, will be used for the title of the entry.
        required: true
        type: str

    username:
        description:
            - Username of the entry.
        required: true
        type: str

    db_password:
        description:
            - Path of the keepass keyfile. Either this or 'keyfile' (or both) are required.
        required: false
        type: str

    entry_password_length:
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
    keyfile: /tmp/vault.key
    title: MariaDB
    username: mariadb-admin
  register: creds
- debug:
    msg: "Username: {{ creds.username }}, Password: {{ creds.password }}, New password: {{ creds.changed }}"

- name: Create a longer new password, or get the existing item
  keepass:
    database: /tmp/vault.kdbx
    keyfile: /tmp/vault.key
    entry_password_length: 45
    title: MariaDB
    username: mariadb-admin
  register: creds
- debug:
    msg: "Username: {{ creds.username }}, Password: {{ creds.password }}, New password: {{ creds.changed }}"

- name: Create a new, host-independent password, or get the existing item
  keepass:
    database: /tmp/vault.kdbx
    keyfile: /tmp/vault.key
    entry_password_length: 45
    title: MariaDB
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
        keyfile=dict(type='str', required=False, default=None),
        db_password=dict(type='str', required=False, default=None, no_log=True),
        entry_password_length=dict(type='int', required=False, default=30, no_log=False),
        title=dict(type='str', required=True),
        username=dict(type='str', required=True),
        entry_password=dict(type='str', required=False, default=None),
        notes=dict(type='str', required=False, default=None),
        expiry_time=dict(type='str', required=False, default=None),
        tags=dict(type='str', required=False, default=None),
        icon=dict(type='str', required=False, default=None),
        url=dict(type='str', required=False, default=None),
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # change is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
        username='',
        entry_password=''
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
    keyfile         = module.params['keyfile']
    db_password        = module.params['db_password']
    entry_password_length = module.params['entry_password_length']
    title         = module.params['title']
    username        = module.params['username']
    entry_password  = module.params['entry_password']
    notes           = module.params['notes']
    expiry_time     = module.params['expiry_time']
    tags            = module.params['tags']
    icon            = module.params['icon']
    url             = module.params['url']
    if not db_password and not keyfile:
        module.fail_json(msg="Either 'password' or 'keyfile' (or both) are required.")

    try:
        kp = PyKeePass(database, password=db_password, keyfile=keyfile)
    except IOError as e:
        KEEPASS_OPEN_ERR = traceback.format_exc()
        module.fail_json(msg='Could not open the database or keyfile.')
    except CredentialsIntegrityError as e:
        KEEPASS_OPEN_ERR = traceback.format_exc()
        module.fail_json(msg='Could not open the database. Credentials are wrong or integrity check failed')

    # try to get the entry from the database
    db_entry = get_entry(module, kp, title)
    user_entry = (title, username, entry_password, url, notes, expiry_time, tags, icon)
    parameter = ('entry.title', 'entry.username','entry.password', 'entry.url', 'entry.notes', 'entry.expiry_time', 'entry.tags', 'entry.icon')
    parameter_name = ('title', 'username', 'password', 'url', 'notes', 'expiry_time', 'tags', 'icon')
    if db_entry:
        if db_entry[0] == title:
            x = range(1, len(db_entry), 1)
            for i in x:
                if user_entry[i] != db_entry[i]:
                    set_param(parameter[i],parameter_name, module, kp, title, username,entry_password, url, notes, expiry_time, tags, icon)
#
#            if entry_password != db_entry_password:
 #               set_entry_password(module, kp, title, entry_password)
#
 #           if notes != db_entry_notes:
  #              set_notes(module, kp, title, notes)
#
 #           if expiry_time != db_entry_expiry_time:
  #              set_expiry_time(module, kp, title, tags)
#
 #           if tags != db_entry_tags:
  #              set_tags(module, kp, title, tags)
#
 #           if icon != db_entry_expiry_time:
  #              set_icon(module, kp, title, icon)
#
            db_entry_title, db_entry_username, db_entry_password, db_entry_url, db_entry_notes, db_entry_expiry_time, db_entry_tags, db_entry_icon = db_entry
            result['title'] = db_entry_title
            result['username'] = db_entry_username
            result['password'] = db_entry_password
            result['url'] = db_entry_url
            result['notes'] = db_entry_notes
            result['expiry_time'] = str(db_entry_expiry_time)
            result['tags'] = db_entry_tags
            result['icon'] = str(db_entry_icon)
            module.exit_json(**result)

    # if there is no matching entry, create a new one
     password = entry_password
    if not module.check_mode:
        try:
            create_entry(module, kp, username, title, password, notes)
        except:
            KEEPASS_SAVE_ERR = traceback.format_exc()
            module.fail_json(msg='Could not add the entry or save the database.', exception=KEEPASS_SAVE_ERR)

    result['title'] = title
    result['username'] = username
    result['password'] = password
    result['notes']    = notes
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


def set_password(module, kp, username, title, password):
    kp.add_entry(kp.root_group, title, username, password, icon='47', notes='Generated by ansible.')
    kp.save()


def get_password(module, kp, username, title):

    entry = kp.find_entries(title=title, first=True)

    if (entry):
        return (entry.title, entry.username, entry.password, entry.url, entry.notes, entry.expiry_time, entry.tags,  entry.icon) #
    else:
        return None


if __name__ == '__main__':
    main()