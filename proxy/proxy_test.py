import requests

# Definiere die Proxies, die auf das Tor-Netzwerk verweisen.
proxies = {
    'http': 'socks5h://localhost:9050',
    'https': 'socks5h://localhost:9050'
}

# Versuche, eine Anfrage durch das Tor-Netzwerk zu senden.
try:
    response = requests.get('http://httpbin.org/ip', proxies=proxies)
    print(response.text)
except requests.RequestException as e:
    print(e)