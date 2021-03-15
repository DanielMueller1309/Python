import os

ip = "192.168.178.10"

file = "hallo"

open("log.txt")

if os.system("ping -c 1 " + ip) == 0:
    file.write.str("IP ist erreichbar")
else:
    file.write.str("IP ist NICHT erreichbar")

