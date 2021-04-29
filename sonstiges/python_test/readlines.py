import os
import subprocess
#temppath zu python holen
tmp = os.environ.get('TMP')
# homepath zu python holen
home = os.environ.get('homepath')

# username zu python holen
user = os.environ.get('username')

newpath_home = home + r'\.UpdateTool'
newpath_tmp = tmp + r'\UpdateTool'

#SID zu python
os.system(r'cmd /c "wmic useraccount where name="%username%" get sid >> %TMP%\UpdateTool\sid.txt"')
mysid = "S-1-5-21-3946235259-77006187-994562352-1001"
file = open(newpath_tmp + r'\sid.txt')
all_lines = file.readlines()
print(all_lines[2])
