#!/usr/bin/env python3.8
import requests
import json
from pydub import AudioSegment

text = "Dieser Text hier ist zum testen der Sprachausgabe gedacht"
voice = {
    "Nicole": "piTKgcLEGmPE4e6mEKli"
}


def teile_text(text, max_laenge=500):
    teile = []  # Liste zum Speichern der Textteile
    aktueller_teil = ""  # Aktueller Textteil, der aufgebaut wird
    satz = ""  # Aktueller Satz, der aufgebaut wird

    for zeichen in text:
        satz += zeichen  # Satz mit jedem Zeichen aufbauen
        # Wenn das Zeichen ein Satzende markiert, prüfe die Länge des aktuellen Teils mit dem Satz
        if zeichen in ".!?":
            if len(aktueller_teil) + len(satz) > max_laenge:
                # Wenn das Hinzufügen des Satzes die maximale Länge überschreiten würde, füge den aktuellen Teil zu den Teilen hinzu
                teile.append(aktueller_teil.strip())
                aktueller_teil = satz  # Beginne einen neuen Teil mit dem aktuellen Satz
            else:
                aktueller_teil += satz  # Füge den Satz zum aktuellen Teil hinzu
            satz = ""  # Setze den Satz zurück für den nächsten Satz

    # Füge den letzten Teil hinzu, falls vorhanden
    if aktueller_teil.strip() != "":
        teile.append(aktueller_teil.strip())

    return teile

def import_json_as_dict(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data

def api_call(text, key, voiceID):
  url = f"https://api.elevenlabs.io/v1/text-to-speech/{voiceID}"

  headers = {
      "Accept": "audio/mpeg",
      "Content-Type": "application/json",
      "xi-api-key": key
  }

  data = {
      "text": text,
      "model_id": "eleven_multilingual_v2",
      "voice_settings": {
          "stability": 0.5,
          "similarity_boost": 0.5
      }
  }

  response = requests.post(url, json=data, headers=headers)
  return response

def convert_to_mp3(response, output_path, CHUNK_SIZE = 1024):
    with open(output_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)

# Define the function to merge mp3 files
def merge_mp3_files(file_paths, output_path):
    combined = AudioSegment.empty()  # Create an empty AudioSegment object

    # Loop through each file in the list and append it to the `combined` AudioSegment
    for file_path in file_paths:
        current_audio = AudioSegment.from_mp3(file_path)  # Load the current MP3 file
        combined += current_audio  # Append it to the combined AudioSegment

    # Export the combined AudioSegment as an MP3 file
    combined.export(output_path, format="mp3")

def main():
  story = """
Die Legende von Lindental: Felix und das Rätsel des Ewigen Brunnens

In einem kleinen Dorf namens Lindental, eingebettet zwischen sanften Hügeln und dichten Wäldern, lebte ein junger Mann namens Felix. Felix war bekannt für seine Abenteuerlust und seinen unermüdlichen Drang, die Welt zu erkunden. Trotz der Warnungen der Dorfbewohner, dass jenseits der Wälder Gefahren lauerten, träumte Felix davon, neue Orte zu entdecken und Geheimnisse zu enthüllen.

Eines Tages, als das Dorf in der warmen Mittagssonne döste, packte Felix seinen Rucksack, nahm seinen treuen Hund Max und verließ heimlich Lindental. Sein Ziel war der verbotene Wald, von dem die Alten sagten, er beherberge ein uraltes Geheimnis.

Die Reise durch den Wald war nicht einfach. Dichtes Unterholz, steile Pfade und das unheimliche Echo unbekannter Tiere begleiteten Felix und Max. Doch Felix' Entschlossenheit wankte nicht. Nach Stunden des Wanderns erreichten sie eine Lichtung, in deren Mitte ein alter, verwitterter Turm stand.

Fasziniert von der Struktur, beschloss Felix, den Turm zu erkunden. Die Tür war überraschend leicht zu öffnen, und im Inneren fanden sie eine Treppe, die in die Tiefe führte. Mit Fackeln ausgestattet, die sie am Eingang fanden, stiegen sie hinab.

Unten angekommen, fanden sie sich in einer großen Halle wieder, die mit Wandmalereien bedeckt war, die Geschichten von alten Königen, magischen Wesen und verborgenen Schätzen erzählten. In der Mitte der Halle stand ein alter Holztisch mit einem staubigen Buch darauf.

Felix näherte sich vorsichtig und schlug das Buch auf. Es war ein Tagebuch, geschrieben von einem Magier namens Alaric, der vor Jahrhunderten gelebt hatte. Das Tagebuch erzählte von Alarics Suche nach der Quelle der ewigen Jugend, einem magischen Brunnen, der tief im Wald verborgen lag.

Getrieben von Neugier und dem Wunsch, sein Dorf zu beeindrucken, beschloss Felix, die Suche nach dem Brunnen fortzusetzen. Mit Hilfe der Hinweise aus dem Tagebuch machten sich Felix und Max auf den Weg durch den Wald, entschlossen, das Geheimnis zu lüften.

Tage vergingen, während sie sich durch dichte Wälder und über Berge kämpften, immer den Anweisungen des Tagebuchs folgend. Schließlich, als sie fast die Hoffnung verloren hatten, stießen sie auf eine verborgene Schlucht, in deren Mitte ein glitzernder Brunnen stand.

Felix konnte seinen Augen kaum trauen. Der Brunnen war wunderschön, umgeben von seltenen Blumen und leuchtenden Steinen. Er näherte sich vorsichtig und sah, wie das Wasser im Sonnenlicht funkelte. Als er seine Hand ins Wasser tauchte, spürte er eine Welle von Energie und Vitalität.

In diesem Moment erkannte Felix, dass die wahre Magie nicht im ewigen Leben lag, sondern in der Reise und den Erfahrungen, die er auf seinem Weg gesammelt hatte. Mit einem Lächeln im Gesicht und Max an seiner Seite machte er sich auf den Weg zurück nach Lindental, bereit, seine Geschichte zu teilen und die Dorfbewohner zu inspirieren, über den Tellerrand hinaus zu denken und ihre eigenen Abenteuer zu erleben.

Als Felix ins Dorf zurückkehrte, wurde er mit offenen Armen empfangen. Die Bewohner hörten gebannt zu, als er von seinen Abenteuern erzählte, und viele wurden von seinem Mut und seiner Entschlossenheit inspiriert. Felix hatte nicht nur das Geheimnis des verbotenen Waldes gelüftet, sondern auch das Herz seiner Mitmenschen berührt.

Von diesem Tag an wurde Felix als der Entdecker von Lindental gefeiert, und seine Geschichte wurde von Generation zu Generation weitererzählt. Der junge Mann, der einst davon geträumt hatte, die Welt zu erkunden, hatte gelernt, dass die größten Schätze oft in den Erfahrungen und den Beziehungen liegen, die wir auf unserer Reise durch das Leben sammeln.
  """
  splited_text =  teile_text(story)
  print(len(splited_text[0]))

  data = import_json_as_dict("./api_keys.json")
  key = data["keys"][0]

  for index, text in enumerate(splited_text,1):
    for key in data["keys"]:
      response = api_call(text, key, voice["Nicole"])
      if response.status_code == 200:
        if index in [5]:
          convert_to_mp3(response, output_path=f"./felix_output_teil{index}.mp3")
        break
      else:
          f"Etwas ist schief gelaufen.\nresponse.status_code: {response.status_code }\nresponse.content:\n{response.content}"


  #file_paths = [f'./felix_output_teil{i}.mp3' for i in range(1, 9)]
  #output_path = "./felix_output_merged"
  ## Merge the MP3 files
  #merge_mp3_files(file_paths, output_path)

if __name__ == "__main__":
    main()

