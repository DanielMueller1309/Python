from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
import random
from selenium.webdriver.common.keys import Keys
from pydub import AudioSegment
import urllib
from urllib import request
import speech_recognition

# Pfad zur Sounddatei
data_path = r"recaptcha_sounds\audio.mp3"
new_data_path = r"recaptcha_sounds\audio.wav"


chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
#Change chrome driver path accordingly
chrome_driver = r"C:\Users\danie\AppData\Local\Programs\Python\chromedriver_win32_v90\chromedriver.exe"
browser = webdriver.Chrome(chrome_driver, options=chrome_options)
browser.switch_to.window(browser.window_handles[0])
print(browser.title)




frames = browser.find_elements_by_tag_name("iframe")
browser.switch_to.frame(frames[0])
time.sleep(random.randint(1, 2))
browser.find_element_by_class_name("recaptcha-checkbox-border").click()
browser.switch_to.default_content()
frames = browser.find_element_by_xpath("html/body/div[2]/div[4]").find_elements_by_tag_name("iframe")
browser.switch_to.frame(frames[0])
time.sleep(random.randint(1, 2))
browser.find_element_by_id("recaptcha-audio-button").click()
browser.switch_to.default_content()
frames = browser.find_elements_by_tag_name("iframe")
browser.switch_to.frame(frames[-1])
time.sleep(random.randint(1, 2))
#error = browser.find_element_by_class_name("rc-audiochallenge-error-message")
error = "xxx"
while error != "":
    browser.find_element_by_xpath("html/body/div/div/div[3]/div/button").click()

    # audio finden und speichern
    src = browser.find_element_by_id("audio-source").get_attribute("src")
    urllib.request.urlretrieve(src, data_path)

    # Umwandeln von mp3 zu wav
    sound = AudioSegment.from_mp3(data_path)
    sound.export(new_data_path, format="wav")

    # Trans-scripting
    recognizer = speech_recognition.Recognizer()
    google_audio = speech_recognition.AudioFile(new_data_path)
    with google_audio as source:
        audio = recognizer.record(source)
    text = recognizer.recognize_google(audio, language='de-DE')
    print("<Erkannter Text> {}".format(text))

    # text in reCaptcha Feld eintragen
    inputfield = browser.find_element_by_id("audio-response")
    inputfield.send_keys(text.lower())
    inputfield.send_keys(Keys.ENTER)
    time.sleep(random.randint(1, 2))
    error = browser.find_element_by_class_name("rc-audiochallenge-error-message").text
os.remove(new_data_path)
os.remove(data_path)