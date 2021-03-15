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