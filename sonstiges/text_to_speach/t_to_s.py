#!/usr/bin/env python3.8
import requests
import json

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
def main():
  story = """
Kapitel 1: Der Erwachte Wald

In der tiefsten Dunkelheit des Erwachten Waldes, wo das Mondlicht nur spärlich durch die dichten Blätterkronen der uralten Bäume drang, erwachte etwas Altes. Etwas, das lange in den Tiefen der Erde geschlummert hatte, geweckt durch die sanften Gesänge der Waldnymphen und das ferne Echo eines Zauberworts, das durch die Nacht hallte.

Am Rand des Waldes, versteckt unter einem Baldachin aus dichtem Laub, lag das kleine Dorf Eldoria, dessen Bewohner von den Geheimnissen des Waldes umgeben lebten, doch selten dessen Schwelle überschritten. Die Legenden des Erwachten Waldes wurden von Generation zu Generation weitergegeben, Geschichten von verlorenen Städten, magischen Kreaturen und uralten Göttern, die in den Tiefen des Waldes schliefen.

In dieser Nacht, unter dem silbernen Schein des Vollmonds, machte sich eine junge Frau namens Lyra, die Tochter des Dorfschmieds, auf den Weg in den Wald. Trotz der Warnungen der Dorfältesten und der besorgten Blicke ihrer Familie fühlte Lyra sich von dem Wald angezogen, als würde etwas Unsichtbares, fast Vergessenes, sie zu sich rufen.

Bewaffnet mit nichts weiter als einer alten, von ihrem Vater geschmiedeten Laterne und einem kleinen Beutel voller Kräuter und Amulette, die sie von ihrer Großmutter geerbt hatte, betrat Lyra den Wald. Der Boden unter ihren Füßen war weich, bedeckt mit einem Teppich aus Moos und gefallenen Blättern, und mit jedem Schritt fühlte sie, wie die alte Magie des Waldes durch ihre Adern pulsierte.

Tief im Herzen des Waldes angekommen, dort, wo die Bäume so hoch waren, dass ihre Spitzen die Sterne zu berühren schienen, fand Lyra eine Lichtung, die von einem sanften, bläulichen Licht erhellt wurde. In der Mitte der Lichtung stand ein alter Steinbrunnen, dessen Wasser in dem Mondlicht zu leuchten schien.

Lyra spürte, dass dies der Ort war, zu dem sie gerufen worden war. Vorsichtig näherte sie sich dem Brunnen und blickte in das klare Wasser. Doch anstatt ihres eigenen Spiegelbildes sah sie Visionen von Ereignissen, die weit in der Vergangenheit lagen, und von Gesichtern, die sie nie gesehen hatte, aber dennoch irgendwie vertraut wirkten.

Plötzlich wurde die Stille der Nacht von einem tiefen, grollenden Laut durchbrochen, der den Boden unter Lyras Füßen erzittern ließ. Aus den Schatten der Bäume trat eine Gestalt hervor, groß und furchteinflößend, mit Augen, die wie zwei glühende Kohlen in der Dunkelheit leuchteten.

Es war ein Wächter des Waldes, eines der alten Wesen, die seit Äonen die Geheimnisse des Waldes hüteten. Mit einer Stimme, die klang wie das Rauschen des Windes durch die Blätter, sprach der Wächter: "Wer wagt es, die Ruhe des Erwachten Waldes zu stören und die Geheimnisse der Alten zu erwecken?"

Lyra, obwohl von Furcht ergriffen, spürte eine unerklärliche Verbundenheit mit dem Wächter. Mit zitternder Stimme antwortete sie: "Ich bin Lyra, Tochter des Schmieds von Eldoria. Ich weiß nicht, was mich hierher geführt hat, aber ich spüre, dass es mein Schicksal ist, die Geheimnisse dieses Waldes zu ergründen."

Der Wächter betrachtete Lyra lange und durchdringend, bevor er schließlich sprach: "In dir fließt das Blut der Alten, Kind des Menschen. Du trägst eine große Bestimmung in dir, doch der Weg, den du zu beschreiten gedenkst, ist voller Gefahren und Prüfungen. Bist du bereit, dein Schicksal anzunehmen und die Geheimnisse zu enthüllen, die tief im Herzen des Erwachten Waldes verborgen liegen?"

Lyra, deren Herz von einer Mischung aus Angst und Entschlossenheit erfüllt war, nickte. In diesem Moment wusste sie, dass ihr Leben nie wieder so sein würde wie zuvor. Sie war bereit, den Pfad zu beschreiten, der vor ihr lag, und die Geheimnisse des Erwachten Waldes zu lüften.

Der Wächter hob seine mächtige Hand und berührte sanft Lyras Stirn. Ein warmes, goldenes Licht umhüllte sie, und sie spürte, wie die alte Magie des Waldes in sie eindrang, ihre Sinne schärfte und ihre Seele mit der Weisheit der Alten erfüllte.

Mit neuen Kräften ausgestattet und vom Wächter des Waldes gesegnet, machte sich Lyra auf den Weg, um das Geheimnis ihrer Bestimmung zu entschlüsseln. Hinter ihr lag das Dorf Eldoria und das Leben, das sie kannte, vor ihr ein Abenteuer, das so alt war wie der Wald selbst.

So beginnt die Reise von Lyra, der Tochter des Schmieds, in die Tiefen des Erwachten Waldes, auf der Suche nach Antworten und der Erfüllung ihres Schicksals. Was sie in den Schatten des Waldes finden wird, ist noch unbekannt, doch eines ist gewiss: Die Geschichte von Lyra und dem Erwachten Wald ist gerade erst begonnen.

  """
  splited_text =  teile_text(story)
  print(len(splited_text[0]))

  data = import_json_as_dict("./api_keys.json")
  key = data["keys"][0]

  for index, text in enumerate(splited_text,1):
    for key in data["keys"]:
      response = api_call(text, key, voice["Nicole"])
      if response.status_code == 200:
        convert_to_mp3(response, output_path=f"./output_teil{index}.mp3")
        break
      else:
          f"Etwas ist schief gelaufen.\nresponse.status_code: {response.status_code }\nresponse.content:\n{response.content}"

if __name__ == "__main__":
    main()

