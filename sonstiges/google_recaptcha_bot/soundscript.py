from pydub import AudioSegment
import speech_recognition

#Pfad des Bots
data_path = r"/sonstiges/google_recaptcha_bot"

#Umwandeln von mp3 zu wav
sound = AudioSegment.from_mp3(data_path + "\\audio.mp3")
sound.export(data_path + "\\audio.wav", format="wav")


#transscripting
Audio_File = data_path + "\\audio.wav"
recognizer = speech_recognition.Recognizer()
google_audio = speech_recognition.AudioFile(data_path + "\\audio.wav")
with google_audio as source:
    audio = recognizer.record(source)
text = recognizer.recognize_google(audio, language='de-DE')
print("<Erkannter Text> {}".format(text))