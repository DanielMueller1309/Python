import os
import requests
from datetime import datetime

# URL des Bildes
image_url = "https://www.dwd.de/DWD/wetter/radar/rad_brd_akt.jpg"

# Zielordner
output_dir = "/home/danie/git/Python/sonstiges/weather_watch/radar_images"

# Ordner erstellen, falls nicht vorhanden
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Zeitstempel für den Dateinamen
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = f"radar_image_{timestamp}.jpg"

# Bild herunterladen und speichern
response = requests.get(image_url)
if response.status_code == 200:
    with open(os.path.join(output_dir, output_file), 'wb') as file:
        file.write(response.content)
    print(f"Bild erfolgreich heruntergeladen und gespeichert in {os.path.join(output_dir, output_file)}")
else:
    print("Fehler beim Herunterladen des Bildes")
