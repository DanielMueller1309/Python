import time
import os
from selenium import webdriver
#from selenium.webdriver.common.keys import Key

# Pfad zum Bot
data_path = r"C:\Users\danie\Git\Python\sonstiges\bookmarkparser"

# browser festlegen
browser = webdriver.Chrome(r"C:\Users\danie\AppData\Local\Programs\Python\chromedriver_win32\chromedriver.exe")


browser.get("chrome://bookmarks/")
browser.find_element_by_id('menuButton').click()
