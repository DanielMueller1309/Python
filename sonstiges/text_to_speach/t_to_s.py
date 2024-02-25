#!/usr/bin/env python3.8
import requests
import json

text = "Dieser Text hier ist zum testen der Sprachausgabe gedacht"
voice = {
    "Nicole": "piTKgcLEGmPE4e6mEKli"
}
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
    with open('output.mp3', 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)
def main():
  data = import_json_as_dict("./api_keys.json")
  response = api_call(text, data["keys"][0], voice["Nicole"])
  convert_to_mp3(response, output_path="./output.mp3")

if __name__ == "__main__":
    main()

