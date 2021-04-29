import os
import time
tmp = os.environ.get('TMP')

# erstelle ordner zum speichern
newpath = tmp + r'\UpdateTool'
if not os.path.exists(newpath):
    os.makedirs(newpath)

#setze aktuelle zeit
now = time.strftime("%m-%d-%y_%H-%M-%S")

# erstelle datei wenn nicht vorhanden
file = open(newpath + r'\datei.txt', 'a+')
file.write("Zeit: " + now + "\n")
file.close()
#file.write("Ich bin eine Datei\n")
