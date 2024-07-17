import os
import requests
from datetime import datetime
import argparse

# Standardpfad ist das Home-Verzeichnis des Benutzers
default_output_dir = os.path.expanduser("~/radar_images")

# Argumentparser einrichten
parser = argparse.ArgumentParser(description='Download weather radar images.')
parser.add_argument('-o','--output_dir', type=str, default=default_output_dir,
                    help='Directory to save the images. Default is the home directory of the user.')

args = parser.parse_args()
output_dir = args.output_dir

# URL des Bildes
image_url = "https://www.dwd.de/DWD/wetter/radar/rad_brd_akt.jpg"

# Zielordner erstellen, falls nicht vorhanden
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
