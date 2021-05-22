import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import platform
system = platform.platform()

if 'Linux' in system:
    tmp = "/tmp"
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
newpath = tmp + slashes +'timestamps'
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
    browser = webdriver.Chrome(options=options, executable_path="/home/user/PycharmProjects/selenium_driver/chromedriver")
    return browser
if 'Linux' in system:
    browser = webdriver_linux()
if 'Windows' in system:
    browser = webdriver_win()

# wechselt zu aktuell offenen tab (sollte hierbei Whatsapp sein)
browser.switch_to.window(browser.window_handles[0])

nutzeranzahl = int(browser.find_element_by_xpath("html/body/div/div[1]/div[1]/div[3]/div/div[2]/div[3]/div/div").get_attribute("aria-rowcount"))
i = 1
# voreinstellung der browser-fenster-höhen
# da bei scrollbarem chatverlauf unerwünschte effekte auftreten wie das nicht alle chats mitgenommen werden
# browserseitiges Zoomen ist nicht zu empfehlen da dadurch .click() nicht jeden nutzer mitnimmt und das script mit den usern durcheinander kommt
# (werte händisch ermittelt)
chrome_hoehe = 121
header_hoehe = 59
sucher_hoehe = 49
archive_hoehe = 49
gesamt_vor_hoehe = chrome_hoehe + header_hoehe + sucher_hoehe + archive_hoehe
chat_hoehe = 73
browser.set_window_size(600, gesamt_vor_hoehe + chat_hoehe * nutzeranzahl)

print("--------------------------------")

while i > 0:
    # prüfe alle nutzer absteigend durch (aufsteigend müsste auch gehen, wurde aber noch nicht getestet)
    for j in range(nutzeranzahl, 0, -1):
        # ermittelt username aus chatverlauf
        username_chatverlauf = browser.find_element_by_xpath("html/body/div/div[1]/div[1]/div[3]/div/div[2]/div[3]/div/div/div[" + str(j) + "]/div/div/div[2]/div[1]/div[1]/span/span")
        print(str(j))
        print("listenname: " + username_chatverlauf.text)
        username_chatverlauf.click()
        # ermittelt username aus angeklickten chat
        chat = browser.find_element_by_xpath("html/body/div/div/div/div[4]/div/header/div[2]")
        username_chat = browser.find_element_by_xpath("html/body/div/div/div/div[4]/div/header/div[2]/div")
        print("chatkopf: "+ username_chat.text)
        # ermittelt onlinestatus
        print("Online-Status: ")
        time.sleep(0.1)
        anzahl = chat.find_elements_by_tag_name("div")
        # wenn zweites div element vorhanden ist wird geprüft ob es das wort online ist oder etwas anderes, bei online logge aktuelle zeit
        if len(anzahl) == 3:
            now = time.strftime("%m-%d-%y_%H-%M-%S")
            status = browser.find_element_by_xpath("html/body/div/div/div/div[4]/div/header/div[2]/div[2]/span").text
            if status == "online":
                print('zuletzt online:' + now)
                in_datei_schreiben()
            else:
                print("offline")
        else:
            print("offline")
        print("--------------------------------")
        time.sleep(1)
