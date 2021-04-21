import time
import os
#zeit festlegen
#now = time.strftime("%m-%d-%y--%H-%M-%S")
temp = os.environ.get('TMP')
newpath = temp + r'\UpdateTool'
if not os.path.exists(newpath):
  os.makedirs(newpath)

#print(now)
