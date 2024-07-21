import asyncio
from pyppeteer import launch
import time

async def screenshot():
    browser = await launch()
    page = await browser.newPage()
    # Setze die Viewport-Größe, falls nötig
    w = 1280 * 1
    h = 800  * 1
    await page.setViewport({'width': w, 'height': h})
    await page.goto('https://radar.wo-cloud.com/desktop/wr/interactive?wrx=51.35,9.27&wrm=5&wrf=true&wry=52.13,11.63')
    time.sleep(15)
    await page.screenshot({'path': 'karte_pyppeteer.png'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(screenshot())
