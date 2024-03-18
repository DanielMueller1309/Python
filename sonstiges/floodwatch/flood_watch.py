import requests
from bs4 import BeautifulSoup

# URL der Seite, von der wir Daten extrahieren möchten
url = 'https://www.pegelonline.wsv.de/gast/pegelinformationen?scrollPosition=0&gewaesser=ELBE'

# Webseite abrufen
response = requests.get(url)

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
            wasserstand_pnp = columns[-2].get_text(strip=True).split('\n')[0]  # Remove ' cm' from the string
            if pegelname != 'Pegelname':
                extracted_data.append((pegelname, wasserstand_pnp))


    for pegel, wasserstand in extracted_data:
        print(f"{pegel}: {wasserstand}")
