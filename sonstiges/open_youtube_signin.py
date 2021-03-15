import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
userdata = r"C:\Users\danie\AppData\Local\Google\Chrome\User Data"
chromedriver = r"C:\Users\danie\AppData\Local\Programs\Python\chromedriver_win32\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument(r"C:\Users\danie\AppData\Local\Google\Chrome\User Data")

browser = webdriver.Chrome(r"C:\Users\danie\AppData\Local\Programs\Python\chromedriver_win32\chromedriver.exe", options=options)
browser.get('https://www.youtube.com/')
browser.find_element_by_id('action-button').click()
#textfeld = browser.find_element_by_id('identifierId')
#.send_keys("dumpmails69@gmail.com")
browser.find_element_by_class_name('OIPlvf').click()
time.sleep(1)
browser.find_element_by_class_name('jO7h3c').click()
time.sleep(1)
browser.find_element_by_id('firstName').send_keys('user')
#time.sleep(1)
browser.find_element_by_id('lastName').send_keys('name')
time.sleep(1)
#browser.find_element_by_class_name('VfPpkd-RLmnJb').click()
browser.find_element_by_id('username').send_keys('dumpmail69@1timeemail.com')
#time.sleep(1)
browser.find_element_by_name('Passwd').send_keys('<password>')
browser.find_element_by_name('ConfirmPasswd').send_keys('<password>')
browser.find_element_by_id('accountDetailsNext').click()
#print(klicker)
#def signin(browser):
#    signin_button = browser.find_el