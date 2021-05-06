import os
import socket
import subprocess
class winvars:
    # temppath zu python holen
    tmp = os.environ.get('TMP')
    # homepath zu python holen
    homepath = os.environ.get('homepath')
    # username zu python holen
    username = os.environ.get('username')
    # hostname zu python holen (import socket)
    host = socket.gethostname()
    hostuser = username + '\\' + host
    # user sid zu python holen (import subprocess)
    raw_mysid = subprocess.Popen("wmic useraccount where name=\"%username%\" get sid", shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    (sid_out, sid_err) = raw_mysid.communicate()
    mysid = str(sid_out[48:91], 'utf-8')
    pass
#othervars:
datapath = r'C:' + winvars.homepath + r'\.UpdateTool\datei.exe'
xmlpath = winvars.tmp + r'\UpdateTool\datei.xml'
uriname = r'\UpdateTool'



# writer to combining echo commands to one return var
def writer(file):
    cmd_command = '"' # set first quotation mark
    file = file.splitlines() # split string to list (split every \n to get one line in one listplace)
    for i in range(0, len(file)): # add echo command from splittet file
        cmd_command = cmd_command + r'echo ' + file[i] + ' >> ' + xmlpath
        if i < len(file)-1: # if current place is not the last
            cmd_command = cmd_command + ' & ' # , add a "&"
        else:
            cmd_command = cmd_command + '"' # and if the last, add last quotation mark
    return cmd_command
#write your xml file here and give specialvars names to change them (like other "Author", "URI", "UserID" or "Command")
xml = r'''<?xml version="1.0" encoding="UTF-16"?>
<Task version="1.2" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <RegistrationInfo>
    <Date>2021-04-28T07:52:50.2538139</Date>
    <Author>Anonymus</Author>
    <URI>uri_name</URI>
  </RegistrationInfo>
  <Triggers>
    <LogonTrigger>
      <Enabled>true</Enabled>
      <UserId>hostuser</UserId>
    </LogonTrigger>
  </Triggers>
  <Principals>
    <Principal id="Author">
      <UserId>user_sid</UserId>
      <LogonType>InteractiveToken</LogonType>
      <RunLevel>LeastPrivilege</RunLevel>
    </Principal>
  </Principals>
  <Settings>
    <MultipleInstancesPolicy>IgnoreNew</MultipleInstancesPolicy>
    <DisallowStartIfOnBatteries>true</DisallowStartIfOnBatteries>
    <StopIfGoingOnBatteries>true</StopIfGoingOnBatteries>
    <AllowHardTerminate>true</AllowHardTerminate>
    <StartWhenAvailable>false</StartWhenAvailable>
    <RunOnlyIfNetworkAvailable>false</RunOnlyIfNetworkAvailable>
    <IdleSettings>
      <Duration>PT10M</Duration>
      <WaitTimeout>PT1H</WaitTimeout>
      <StopOnIdleEnd>true</StopOnIdleEnd>
      <RestartOnIdle>false</RestartOnIdle>
    </IdleSettings>
    <AllowStartOnDemand>true</AllowStartOnDemand>
    <Enabled>true</Enabled>
    <Hidden>false</Hidden>
    <RunOnlyIfIdle>false</RunOnlyIfIdle>
    <WakeToRun>false</WakeToRun>
    <ExecutionTimeLimit>PT72H</ExecutionTimeLimit>
    <Priority>7</Priority>
  </Settings>
  <Actions Context="Author">
    <Exec>
      <Command>exe_path</Command>
    </Exec>
  </Actions>
</Task> '''


# lösche falls nötig alte xml datei
if os.path.exists(xmlpath):
    os.remove(xmlpath)

# change specialvars with vars from winvars and other python vars
# notice "<" ">" needs to escape when using in win cmd echo command
xml = xml.replace("<", "^<")
xml = xml.replace(">", "^>")
#to change some dynamic stuff for xml file
xml = xml.replace("hostuser", winvars.hostuser)
xml = xml.replace("user_sid", winvars.mysid)
xml = xml.replace("exe_path", datapath)
xml = xml.replace("uri_name", uriname)

os.system(r'cmd /c ' + writer(xml) )

print('fertig')