# PYTHON Example
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
#Change chrome driver path accordingly
chrome_driver = r"C:\Users\danie\AppData\Local\Programs\Python\chromedriver_win32_v90\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, options=chrome_options)
driver.switch_to.window(driver.current_window_handle)
time.sleep(1)
print(driver.title)
# PYTHON Example
import time
#from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
#i = 1
#browser = webdriver.Chrome(r"C:\Users\danie\AppData\Local\Programs\Python\chromedriver_win32_v90\chromedriver.exe")
##while i > 0:
#chrome_options = Options()
#chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
##Change chrome driver path accordingly
#chrome_driver = r"C:\Users\danie\AppData\Local\Programs\Python\chromedriver_win32_v90\chromedriver.exe"
#driver = webdriver.Chrome(chrome_driver, options=chrome_options)
#driver.switch_to.window()

#driver.switch_to.window(driver)

#driver.refresh()

#print(driver.title)
#time.sleep(1)



# import os
#from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# browser festlegen
#browser = webdriver.Chrome(r"C:\Users\danie\AppData\Local\Programs\Python\chromedriver_win32_v90\chromedriver.exe")

#current window
#first_tab = browser.window_handles[0]
#create new tab
#browser.execute_script("window.open()")
#move to new tab
#new_tab = browser.window_handles[1]
#browser.switch_to.window(new_tab)
#browser.get('https://gmail.com')
#switch to first tab
#browser.switch_to.window(first_tab)
#print(browser.session_id)



#print (browser.window_handles[0])
#browser.switch_to.window(browser.window_handles[0])
#browser.window_handles[1].execute_script("window.open()")
#browser.get(w)
#browser.switch_to.window(browser.current_window_handle)
#print("Current Page Title is : %s" %browser.title)