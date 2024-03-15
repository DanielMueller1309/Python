import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
import random
import time
import json

# Konfigurationsdaten aus JSON-Datei lesen
with open('config.json', 'r') as file:
    config = json.load(file)

bucket = config['bucket']
org = config['org']
token = config['token']
url = config['url']


client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org
)

# Schreib-API
write_api = client.write_api(write_options=SYNCHRONOUS)

def write_random_temperature():
    # Zufälligen Temperaturwert erzeugen
    temperature = random.uniform(20.0, 30.0)

    # Datenpunkt mit zufälliger Temperatur
    p = influxdb_client.Point("my_measurement").tag("location", "Prague").field("temperature", temperature)

    # Datenpunkt schreiben
    write_api.write(bucket=bucket, org=org, record=p)
    print(f"Written data: Location=Prague, Temperature={temperature}°C")

# Hauptteil des Skripts
if __name__ == "__main__":
    while True:
        write_random_temperature()
        # Warte 60 Sekunden bis zur nächsten Schreiboperation
        time.sleep(5)
