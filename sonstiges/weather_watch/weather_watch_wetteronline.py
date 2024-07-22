import asyncio
from pyppeteer import launch
import time
import argparse
import os
from datetime import datetime

# Standardpfad ist das Home-Verzeichnis des Benutzers
default_output_dir = os.path.expanduser("~/wetteronline_radar_images")
# Argumentparser einrichten
parser = argparse.ArgumentParser(description='Download weather radar images.')
parser.add_argument('-o','--output_dir', type=str, default=default_output_dir,
                    help='Directory to save the images. Default is the home directory of the user.')

args = parser.parse_args()
output_dir = args.output_dir

# Zielordner erstellen, falls nicht vorhanden
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Zeitstempel für den Dateinamen
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = f"radar_image_{timestamp}.jpg"
# Zielordner erstellen, falls nicht vorhanden
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Zeitstempel für den Dateinamen
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = f"radar_image_{timestamp}.jpg"
async def screenshot():
    browser = await launch()
    page = await browser.newPage()
    # Setze die Viewport-Größe, falls nötig
    #w = 1280 * 1
    #h = 800  * 1
    w = 2560
    h = 1600
    await page.setViewport({'width': w, 'height': h})
    await page.goto('https://radar.wo-cloud.com/desktop/wr/interactive?wrx=50.89,9.94&wrm=7&wrp=periodCurrentHighRes&wrf=true')
    time.sleep(10)
    await page.screenshot({'path': f'{os.path.join(output_dir, output_file)}'})
    await browser.close()


asyncio.get_event_loop().run_until_complete(screenshot())
