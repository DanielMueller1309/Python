import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
tmp = os.environ.get('TMP')


# erstelle ordner zum speichern
newpath = tmp + r'\timestamps'
if not os.path.exists(newpath):
    os.makedirs(newpath)

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = r"C:\Users\danie\AppData\Local\Programs\Python\chromedriver_win32_v90\chromedriver.exe"
browser = webdriver.Chrome(chrome_driver, options=chrome_options)
browser.switch_to.window(browser.window_handles[0])
#tab_sum = len(browser.window_handles)
#for i in range(tab_sum):
#    title = browser.window_handles[i]
#    print(title)

chatlist = browser.find_element_by_xpath("html/body/div/div[1]/div[1]/div[3]/div/div[2]/div[1]/div/div").text
#print()
anzahl = (chatlist.count("\n") + 1) // 3
print(anzahl)
print("fertig")
for i in range(1, anzahl+1):
    username = browser.find_element_by_xpath("html/body/div/div[1]/div[1]/div[3]/div/div[2]/div[1]/div/div/div[" + str(i) + "]/div/div/div[2]/div[1]/div[1]/span/span").text
    browser.find_element_by_xpath("html/body/div/div[1]/div[1]/div[3]/div/div[2]/div[1]/div/div/div[" + str(i) + "]/div").click()
    print(username)

