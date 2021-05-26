import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import platform
system = platform.platform()
driverpath = "/home/user/Schreibtisch/ChromeDriver_91.0.4472.19/chromedriver"
if 'Linux' in system:
    tmp = "/home/user"
    slashes = '/'
if 'Windows' in system:
    tmp = os.environ.get('TMP')
    slashes = '\\'

# erstelle datei wenn nicht vorhanden
def in_datei_schreiben():
    now = time.strftime("%m-%d-%y_%H-%M-%S")
    file = open(newpath + slashes + username_chat.text + '.txt', 'a+')
    file.write(username_chat.text + '    ' + 'zuletzt online:' + now + "\n")
    file.close()

# erstelle ordner zum speichern
newpath = tmp + slashes +'whatsapp_timestamps'
if not os.path.exists(newpath):
    os.makedirs(newpath)

# setze wendriver auf chrome debugger fenster

#windows
def webdriver_win():
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = r"C:\Users\danie\AppData\Local\Programs\Python\chromedriver_win32_v90\chromedriver.exe"
    browser = webdriver.Chrome(chrome_driver, options=chrome_options)
    return browser
#linux
def webdriver_linux():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    browser = webdriver.Chrome(options=options, executable_path=driverpath)
    return browser
if 'Linux' in system:
    browser = webdriver_linux()
if 'Windows' in system:
    browser = webdriver_win()
# testet ob gelbe Warnung das handy nicht verbunden ist existiert und bleibt in der schleife bis connection wieder da ist
def test_connection():
    oflinetester = browser.find_element_by_xpath("html/body/div/div[1]/div[1]/div[3]/div")  # .find_elements_by_tag_name("span")
    while "Telefon nicht verbunden" in oflinetester.text:
        print("Telefon nicht verbunden...warte")
        time.sleep(3)
#div wert falls wieder probleme auftreten
div_wert = 3

#xpath variablen
left_sidebar_all_xpath = "html/body/div/div[1]/div[1]/div[3]/div"
chatlist_xpath = left_sidebar_all_xpath + "/div[2]/div[" + str(div_wert) + "]/div/div"
archiviert_xpath = left_sidebar_all_xpath + "/div[2]/div[1]"
chat_xpath = "html/body/div/div/div/div[4]/div/header/div[2]"
chat_username_xpath = chat_xpath + "/div"
onlinestatus_xpath = chat_xpath + "/div[2]/span"

# wechselt zu aktuell offenen tab (sollte hierbei Whatsapp sein)
browser.switch_to.window(browser.window_handles[0])
test_connection()

# ermittelt nutzeranzahl
chatlist = browser.find_element_by_xpath(chatlist_xpath)
nutzeranzahl = int(chatlist.get_attribute("aria-rowcount"))
i = 1

# voreinstellung der browser-fenster-höhen
# da bei scrollbarem chatverlauf unerwünschte effekte auftreten (nicht alle chats werden mitgenommen)
# browserseitiges Zoomen ist nicht zu empfehlen da dadurch .click() nicht jeden nutzer mitnimmt und das script mit den usern durcheinander kommt
browser.set_window_size(0, 0) # verkleinerung auf 0 um wirkliche Windowgröße zu ermitteln mit nachfolgendem browser.get_window_size().get("height")
chrome_hoehe = browser.get_window_size().get("height")
header_hoehe = browser.find_element_by_xpath(left_sidebar_all_xpath + "/header").rect.get("height")
offline_banner = 107 # bleibt erst mal hardgecocodet da eine parametrisierung zwar möglich aber wenig sinnvoll ist
sucher_hoehe = browser.find_element_by_xpath(left_sidebar_all_xpath + "/div[1]").rect.get("height")
archive_hoehe = browser.find_element_by_xpath(archiviert_xpath).rect.get("height")
gesamt_vor_hoehe = chrome_hoehe + header_hoehe + offline_banner + sucher_hoehe + archive_hoehe
chat_hoehe = browser.find_element_by_xpath(chatlist_xpath + "/div[1]").rect.get("height")
browser.set_window_size(600, gesamt_vor_hoehe + chat_hoehe * nutzeranzahl)

print("--------------------------------")

while i > 0:
    # prüfe alle nutzer absteigend durch (aufsteigend müsste auch gehen, wurde aber noch nicht getestet)
    for j in range(nutzeranzahl, 0, -1):
        test_connection()
        # ermittelt username aus chatverlauf
        username_chatverlauf = browser.find_element_by_xpath(chatlist_xpath + "/div[" + str(j) + "]/div/div/div[2]/div[1]/div[1]/span/span")
        print(str(j))
        print("listenname: " + username_chatverlauf.text)
        username_chatverlauf.click()
        # ermittelt username aus angeklickten chat
        chat = browser.find_element_by_xpath(chat_xpath)
        username_chat = browser.find_element_by_xpath(chat_username_xpath)
        # zeigt chatheader noch einmal an um überprüfen zu können ob script sauber läuft
        print("chatkopf: " + username_chat.text)
        # ermittelt onlinestatus
        print("Online-Status: ")
        time.sleep(0.1)
        anzahl = chat.find_elements_by_tag_name("div")
        # wenn zweites div element vorhanden ist wird geprüft ob es das wort "online" ist oder etwas anderes, bei online logge aktuelle zeit
        if len(anzahl) == 3:
            now = time.strftime("%m-%d-%y_%H-%M-%S")
            status = browser.find_element_by_xpath(onlinestatus_xpath).text
            if status == "online":
                print('zuletzt online:' + now)
                in_datei_schreiben()
            else:
                print("offline")
        else:
            print("offline")
        print("--------------------------------")
#        time.sleep(1)
