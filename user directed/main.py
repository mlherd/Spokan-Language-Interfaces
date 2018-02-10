import pyttsx
import flow
import googleSpeech as google
import recorder as rec
import time

global introduction
# our project id
project_id = "sli-hw2"
# fake session id
session_id = "1-1-1-1-1"
#String list for user input
texts = [""]

introduction = 0

# initilize the text to speech engine
engine = pyttsx.init()

# introducntion module for first run
def intro():
    engine.say('Hi')
    engine.runAndWait()
    engine.say('How can I help you?')
    engine.runAndWait()

while(True):
    #if it is the first run
    if introduction == 0:
        intro()
        introduction = 1  
        
    # otherwise listen to user for input
    else:
        print("listening")
        # record for 3 seconds
        rec.record()
        # do speechrecognition with the reocrded audio file 
        texts[0], c_rate = google.recognize()
        
        # if the confidence rate us more than 90% send it to dialogflow
        if int(round(float(c_rate)))*10 > 9:
            system = flow.detect_intent_texts(project_id, session_id, texts, 'en-US')
            # get dialog flow response and speak it
            engine.say(system)
            engine.runAndWait()
            # clean the user input
            texts[0] = ""
            
        # if the confidence rate is less than 90% ask user to repeat
        else:
            engine.say('Say something') # :)
            engine.runAndWait()
