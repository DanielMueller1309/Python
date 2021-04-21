import time
import os
#zeit festlegen
#now = time.strftime("%m-%d-%y--%H-%M-%S")
#temp = os.environ.get('TMP')
home = os.environ.get('homepath')

newpath = home + r'\.UpdateTool'
if not os.path.exists(newpath):
  os.makedirs(newpath)

#print(now)
