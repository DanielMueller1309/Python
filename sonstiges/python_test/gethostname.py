import os
import subprocess
username = os.environ.get('username')

raw_mysid = subprocess.Popen("wmic useraccount where name=\"%username%\" get sid", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
(out, err) = raw_mysid.communicate()


mysid = str(out[48:91], 'utf-8')

print("Clean: " + str(mysid))


#proc = subprocess.Popen(["cat", "/etc/services"], stdout=subprocess.PIPE, shell=True)
#print("program output:", raw_mysid)
#print "program output:", out


#hostname zu python holen (etwas anders da hostname keine var)
#raw_host = os.popen('hostname').read()
#host = raw_host[0:len(raw_host)-1]
# username zu python holen
#user = os.environ.get('username')


#hostuser = host + '\\' +user
#print(hostuser)
#username = os.environ.get('username')
#raw_mysid = os.popen('wmic useraccount where name="' + username + '" get sid').read()
#print('das ist die sid:')
#print('Länge:' + str(len(mysid)))
#print(mysid[47:90])
#print('fertig')
