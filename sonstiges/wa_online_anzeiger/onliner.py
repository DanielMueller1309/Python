import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
tmp = os.environ.get('TMP')

# erstelle datei wenn nicht vorhanden
def in_datei_schreiben():
    now = time.strftime("%m-%d-%y_%H-%M-%S")
    file = open(newpath + '\\' + name + '.txt', 'a+')
    file.write(name + '    ' + 'zuletzt online:' + now + "\n")
    file.close()

# erstelle ordner zum speichern
newpath = tmp + r'\timestamps'
if not os.path.exists(newpath):
    os.makedirs(newpath)

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = r"C:\Users\danie\AppData\Local\Programs\Python\chromedriver_win32_v90\chromedriver.exe"
browser = webdriver.Chrome(chrome_driver, options=chrome_options)
browser.switch_to.window(browser.window_handles[0])
chatlist = browser.find_element_by_xpath("html/body/div/div[1]/div[1]/div[3]/div/div[2]/div[1]/div/div").text
nutzeranzahl = int((chatlist.count("\n") + 1) // 3)
i = 1
while i > 0:
    #j = int(1)
    for j in range(1, nutzeranzahl+1):
        username = browser.find_element_by_xpath("html/body/div/div[1]/div[1]/div[3]/div/div[2]/div[1]/div/div/div[" + str(j) + "]/div/div/div[2]/div[1]/div[1]/span/span").text
        #print("listenname: " + username)
        listenplatz = browser.find_element_by_xpath("html/body/div/div[1]/div[1]/div[3]/div/div[2]/div[1]/div/div/div[" + str(j) + "]")
        listenplatz.click()
        user = browser.find_element_by_xpath("html/body/div/div/div/div[4]/div/header/div[2]")
        name = browser.find_element_by_xpath("html/body/div/div/div/div[4]/div/header/div[2]/div").text
        print("chatkopf: "+name)
        time.sleep(0.1)
        anzahl = user.find_elements_by_tag_name("div")
        if len(anzahl) == 3:
            now = time.strftime("%m-%d-%y_%H-%M-%S")
            status = browser.find_element_by_xpath("html/body/div/div/div/div[4]/div/header/div[2]/div[2]/span").text
            if status == "online":
                print(name + '    ' + 'zuletzt online:' + now)
                in_datei_schreiben()

        #j += 1


#file.write("Ich bin eine Datei\n")
#print(status.text)
#pfad zu online status: /html/body/div/div/div/div[4]/div/header/div[2]/div[2]/span
