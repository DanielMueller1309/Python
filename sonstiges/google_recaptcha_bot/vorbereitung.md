#reCAPTCHA
Die Problemstellung ist hierbei ein reCAPTCHA von google mit google spracherkennung zu lösen

###Vorbereitung
####Ablauf
1. Seite mit reCAPTCHA aufrufen
1. Frame mit reCAPTCHA suchen
1. warten
1. Checkbox bestätigen
1. warten
1. audio-challenge auswählen
1. warten
1. audio_challenge anhören
1. link mit audio-challenge finden und herunterladen
1. audo-challenge mit google-voice-recognition in text umwandeln
1. text eingeben und bestätigen

#### Installation
- [FFmpeg installieren](https://ffmpeg.org/)

    Hierbei ist wichtig zu wissen, dass der Ordner __bin__ ffmpeg.exe, ffplayer.exe und ffprobe beinhalten muss.

- [chromedriver installieren](https://chromedriver.chromium.org/downloads)
    
    (passende version wählen) in der ZIP version downloaden

- extrahierte ZIP Ordner in python Pfad ablegen: `C:\Users\danie\AppData\Local\Programs\Python\`

- windows systemvariable bearbeiten 
- über windows suchen umgebungsvariable `Path` bearbeiten
- als neuen eintrag: `C:\Users\danie\AppData\Local\Programs\Python\<Ordnernamen>` für chromedriver und ffmpeg setzen und schließen
- cmd öffnen und `ffmpeg` eingeben sollte zu keinem fehler führen

```
pip install Selenium
pip install pydub
pip install webdriver-manager
pip install SpeechRecognition
```
#### Installation Remote Debugging:
1. Add Chrome to PATH
    - über windows suchen umgebungsvariable `Path` bearbeiten und pfad zu `chrome.exe` hinzufügen.
      (ohne zusatz zur exe sonst geht es nicht, siehe obere beispiele in der `PATH` variable)
      
1. Launch browser with custom flags
    > chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\ChromeProfile"
   - mit diesem command wird eine neue chrome session aufgemacht welche remote debugging auf port 9222 erlaubt.
   - danach dort mit Goggle Konto anmelden und dort weiterarbeiten. 
   - unter [127.0.0.1:9222](http://127.0.0.1:9222) kann man in einem anderen browser nun auf die Debugging-Umgebung zugreifen
Code(Windows):
```python
# PYTHON Example
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
#Change chrome driver path accordingly
chrome_driver = "<python_chrome_driver_path>"
driver = webdriver.Chrome(chrome_driver, options=chrome_options)
print(driver.title)
```     
Code(Linux):
```python
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
browser = webdriver.Chrome(options=options, executable_path="<python_chrome_driver_path>")
browser.switch_to.window(browser.window_handles[0])
```
Quelle: https://cosmocode.io/how-to-connect-selenium-to-an-existing-browser-that-was-opened-manually/   