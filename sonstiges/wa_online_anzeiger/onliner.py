import time
import os
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from pydub import AudioSegment
import urllib
from urllib import request
import speech_recognition
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = r"C:\Users\danie\AppData\Local\Programs\Python\chromedriver_win32_v90\chromedriver.exe"
browser = webdriver.Chrome(chrome_driver, options=chrome_options)
browser.switch_to.window(browser.window_handles[0])
title = browser.title
print(title)
#pfad zu online status: /html/body/div/div/div/div[4]/div/header/div[2]/div[2]/span
