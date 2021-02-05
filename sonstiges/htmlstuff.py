import urllib.request

url = "https://zoom.us/wc/join/7243299415?wpk=wcpk2af5336e013ea6de35408ba2e3c9f298"

status_code = urllib.request.urlopen(url).getcode()
website_is_up = status_code == 200
if str(website_is_up) == "True":
    print("Ja die website ist da")
print(website_is_up)