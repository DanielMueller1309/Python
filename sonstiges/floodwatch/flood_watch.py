#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import time
from stem import Signal
from stem.control import Controller
import json
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
import argparse


# ArgumentParser erstellen
parser = argparse.ArgumentParser(description="Dem flood_watch Skript können mehrere Argumtente übergeben werden")
# Erforderliche Argumente hinzufügen
parser.add_argument("-c", "--influxdb-config-file", type=str, default="./influxdb_config.json", help="Pfad zur Konfigurationsdatei.")
parser.add_argument("-p", "--tor-password-file", type=str, default="./password.json", help="Pfad zur Passwortdatei.")
# Argumente parsen
args = parser.parse_args()

# URL der Seite, von der wir Daten extrahieren möchten
url = 'https://www.pegelonline.wsv.de/webservices/rest-api/v2/stations.json?includeTimeseries=true&includeCurrentMeasurement=true'


# load tor control port pw
with open(f'{args.tor_password_file}', 'r') as file:
    control_port_password = json.load(file)

# InfluxDB Konfigurationsdaten aus JSON-Datei lesen
with open(f'{args.influxdb_config_file}', 'r') as file:
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
    # ausschluss von ['PRELOUC',]
    exclude_list_for_pegel_call = [""]
    extracted_data = []
    pegel_response = requests.get(url, proxies=proxies)
    r = json.loads(pegel_response.text)
    print("")
    for item in r:
      if item['water']['shortname'] == 'ELBE':
        pegelname = item['shortname']
        km = float(item['km'])
        if "timeseries" in item:
            for series in item["timeseries"]:
                if series["shortname"] == "W":
                  wasserstand = float(series["currentMeasurement"]["value"])

                  extracted_data.append((pegelname, km, wasserstand))
    # debug
    #for pegel, km, wasserstand in extracted_data:
    #    print(f"{pegel}({km}km): {wasserstand}")
    #return extracted_data


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
      # for debug
      #print(f"Written data: Location={location}({km}km), Wasserstand={wasserstand}cm")


def main():
  data = call_pegel()
  push_to_influxdb(data)
  renew_tor_connection()


if __name__ == "__main__":
      main()
