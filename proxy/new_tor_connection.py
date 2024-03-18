import time
from stem import Signal
from stem.control import Controller
import json
import requests


# load pw
with open('password.json', 'r') as file:
    password = json.load(file)
# Dein festgelegtes Passwort für den Control Port
control_port_password = password["password"]


# Definiere die Proxies, die auf das Tor-Netzwerk verweisen.
proxies = {
    'http': 'socks5h://localhost:9050',
    'https': 'socks5h://localhost:9050'
}

# Versuche, eine Anfrage durch das Tor-Netzwerk zu senden.
def make_request():
  try:
      response = requests.get('http://httpbin.org/ip', proxies=proxies)
      print(response.text)
  except requests.RequestException as e:
      print(e)


def renew_tor_connection():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password=control_port_password)
        controller.signal(Signal.NEWNYM)

# Alle Stunde Tor neu verbinden
while True:
    make_request()
    renew_tor_connection()
    print("Tor connection renewed.")
    # 3600 Sekunden warten (1 Stunde)
    time.sleep(10)
