import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

global text
global conf
conf = "0"
text = "**"

def recognize():
    global text
    global conf
    # Instantiates a client
    client = speech.SpeechClient()
    # The name of the audio file to transcribe
    file_name = 'output.wav'
    # Loads the audio into memory
    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='en-US')
    # Detects speech in the audio file
    response = client.recognize(config, audio)

    for result in response.results:
        text = str(result.alternatives[0].transcript)
        conf = str(result.alternatives[0].confidence)

    return text, conf
