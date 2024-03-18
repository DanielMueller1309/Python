import requests
from bs4 import BeautifulSoup
import time
from stem import Signal
from stem.control import Controller
import json
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

# URL der Seite, von der wir Daten extrahieren möchten
url = 'https://www.pegelonline.wsv.de/gast/pegelinformationen?scrollPosition=0&gewaesser=ELBE'


# load tor control port pw
with open('password.json', 'r') as file:
    control_port_password = json.load(file)

# InfluxDB Konfigurationsdaten aus JSON-Datei lesen
with open('influxdb_config.json', 'r') as file:
    influxdb_config = json.load(file)

# Definiere die Proxies, die auf das Tor-Netzwerk verweisen.
proxies = {
    'http': 'socks5h://localhost:9050',
    'https': 'socks5h://localhost:9050'
}

def renew_tor_connection():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password=control_port_password["password"])
        controller.signal(Signal.NEWNYM)

def call_pegel():
  # Webseite abrufen
  response = requests.get(url, proxies=proxies)
  
  # Stelle sicher, dass die Anfrage erfolgreich war
  if response.status_code == 200:
      soup = BeautifulSoup(response.content, 'html.parser')
      data_rows = soup.find_all("tr", {"class": ["tablerow1", "tablerow2"]})
  
      # Adjusting column selection to correctly extract "Wasserstand relativ zum PNP"
      extracted_data = []
  
      for row in data_rows:
          columns = row.find_all("td")
          if columns:
              pegelname = columns[0].get_text(strip=True)
              km = columns[2].get_text(strip=True)
              wasserstand_pnp = columns[-2].get_text(strip=True).split('\r')[0]
              if pegelname != 'Pegelname':
                  wasserstand = float(wasserstand_pnp)
                  extracted_data.append((pegelname, km, wasserstand))
      for pegel, km, wasserstand in extracted_data:
          print(f"{pegel}({km}km): {wasserstand}")
      return extracted_data

def push_to_influxdb(data):
    client = influxdb_client.InfluxDBClient(
        url=influxdb_config['url'],
        token=influxdb_config['token'],
        org=influxdb_config['org']
    )

    # Schreib-API
    write_api = client.write_api(write_options=SYNCHRONOUS)

    # Datenpunkte erstellenx
    for location, km, wasserstand in data:
      p = influxdb_client.Point("pegelstand") \
          .tag("location", f"{location}") \
          .tag("km", f"{km}") \
          .field("wasserstand", wasserstand)

      # Datenpunkt schreiben
      write_api.write(bucket=influxdb_config['bucket'], org=influxdb_config['org'], record=p)
      print(f"Written data: Location={location}({km}km), Wasserstand={wasserstand}cm")


def main():
  data = call_pegel()
  push_to_influxdb(data)
  renew_tor_connection()


if __name__ == "__main__":
      main()
