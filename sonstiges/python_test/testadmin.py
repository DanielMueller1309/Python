import os

# homepath zu python holen
home = os.environ.get('homepath')
#os.system(r'cmd /c "schtasks /create /sc onlogon /it /tn UpdateTool /tr ' + home + r'\.UpdateTool\testtask.exe"')