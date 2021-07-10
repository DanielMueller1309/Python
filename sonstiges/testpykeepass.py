from pykeepass import PyKeePass
# load database
kp = PyKeePass(r'C:\Users\danie\Git\ansible\ansible_home\test_db.kdbx', password='hallowelt')
group = kp.groups
#kp.add_entry(destination_group='test_db',title='testentry', username='testusername', password='testpw')
#kp.add_group(kp.root_group, 'test_addgroup')
kp.add_entry(destination_group=group[2], title='testentry', username='testusername', password='testpw')
kp.save()
print('ende')
