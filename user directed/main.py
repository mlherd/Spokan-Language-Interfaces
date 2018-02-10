import pyttsx
import flow
import googleSpeech as google
import recorder as rec
import time

global introduction
project_id = "sli-hw2"
session_id = "1-1-1-1-1"
texts = [""]

introduction = 0

engine = pyttsx.init()

def intro():
    engine.say('Hi')
    engine.runAndWait()
    engine.say('How can I help you?')
    engine.runAndWait()

while(True):
    if introduction == 0:
        intro()
        introduction = 1   
    else:
        print("listening")
        rec.record()
        texts[0], c_rate = google.recognize()
        if int(round(float(c_rate)))*10 > 9:
            system = flow.detect_intent_texts(project_id, session_id, texts, 'en-US')
            engine.say(system)
            engine.runAndWait()
            texts[0] = ""
        else:
            engine.say('Say something')
            engine.runAndWait()
