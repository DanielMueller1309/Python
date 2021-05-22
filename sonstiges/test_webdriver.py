from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import platform
from selenium.webdriver.common.keys import Keys



#windows
def webdriver_win():
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = r"C:\Users\danie\AppData\Local\Programs\Python\chromedriver_win32_v90\chromedriver.exe"
    browser = webdriver.Chrome(chrome_driver, options=chrome_options)
    browser.switch_to.window(browser.window_handles[0])

#linux
def webdriver_linux():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    browser = webdriver.Chrome(options=options, executable_path="/home/user/PycharmProjects/selenium_driver/chromedriver")
    browser.switch_to.window(browser.window_handles[0])

system = platform.platform()
print(system)

if 'Linux' in system:
    webdriver_linux()
if 'Windows' in system:
    webdriver_win()

