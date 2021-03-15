mkdir ~/phone_track
cd /phone_track


git clone https://github.com/thewhiteh4t/seeker.git
cd seeker/
apt update
apt install python3 python3-pip php
pip3 install requests



git clone https://github.com/thewhiteh4t/seeker
cd /seeker
chmod +x install.sh
sudo ./seeker.py
sudo ./seeker.py -t manual


#### in another terminal (tmux pane)
####https://ngrok.com/download besuchen für passenden linux wget link
wget -P ~/ https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
unzip ngrok-stable-linux-amd64.zip
./ngrok http 8080
