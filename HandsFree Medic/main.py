import pyttsx
import googleSpeech as google
import recorder as rec

p_name = False
p_temp = False
p_pulse = False
p_pain = False

file = None
engine = pyttsx.init()

# methods for system directed messeges
def intro():
    engine.say('Hi')
    engine.runAndWait()
    engine.say('This is a Hands Free Medic App')
    engine.runAndWait()

def name():
    engine.say('Whats is patients name:')
    engine.runAndWait()

def temp():
    engine.say('Whats is patients temperature:')
    engine.runAndWait()

def pulse():
    engine.say('Whats is patients pulse rate:')
    engine.runAndWait()

def pain():
    engine.say('Whats is patients pain level:')
    engine.runAndWait()
    engine.say('one to ten')
    engine.runAndWait()

def end():
    engine.say('Patient data is saved')
    engine.runAndWait()
    file.close()

#call introduction method to start the app
intro()

# get the paitient name
while p_name == False:
    name()
    rec.record()
    text, c_rate = google.recognize()
    if int(round(float(c_rate)))*10 > 9:
        engine.say('You said')
        print "You said " + text
        engine.say(text)
        engine.runAndWait()
        yes = False
        while yes == False:
            engine.say('Yes or No')
            engine.runAndWait()
            rec.record()
            yn_text, c_rate = google.recognize()
            if yn_text == "yes" or yn_text == "YES" or yn_text == "Yes":
                p_name = True
                yes = True
                file_name = str(text) + ".txt"
                file = open(file_name,"w")
                name = "name: " + str(text) + '\n'
                file.write(name)
            elif yn_text == "no" or yn_text == "NO" or yn_text == "No":
                p_name = False
                yes = True
                engine.say('Okay we should try again')
                engine.runAndWait()
            else:
                p_name = False
                yes = False
    elif text == "**":
        engine.say('I did not get that')
        engine.runAndWait()
        p_name = False

# get the temperature
while p_temp == False:
    temp()
    rec.record()
    text, c_rate = google.recognize()
    if int(round(float(c_rate)))*10 > 9:
        engine.say('You said')
        print "You said " + text
        engine.say(text)
        engine.runAndWait()
        yes = False
        while yes == False:
            engine.say('Yes or No')
            engine.runAndWait()
            rec.record()
            yn_text, c_rate = google.recognize()
            if yn_text == "yes" or yn_text == "YES" or yn_text == "Yes":
                p_temp = True
                yes = True
                t = "temperature: " + str(text) + '\n'
                file.write(t)
            elif yn_text == "no" or yn_text == "NO" or yn_text == "No":
                p_temp = False
                yes = True
                engine.say('Okay we should try again')
                engine.runAndWait()
            else:
                p_temp = False
                yes = False
    elif text == "**":
        engine.say('I did not get that')
        engine.runAndWait()
        p_temp = False

# get pulse rate
while p_pulse == False:
    pulse()
    rec.record()
    text, c_rate = google.recognize()
    if int(round(float(c_rate)))*10 > 9:
        engine.say('You said')
        print "You said " + text
        engine.say(text)
        engine.runAndWait()
        yes = False
        while yes == False:
            engine.say('Yes or No')
            engine.runAndWait()
            rec.record()
            yn_text, c_rate = google.recognize()
            if yn_text == "yes" or yn_text == "YES" or yn_text == "Yes":
                p_pulse = True
                yes = True
                p = "pulse: " + str(text) + '\n'
                file.write(p)
            elif yn_text == "no" or yn_text == "NO" or yn_text == "No":
                p_pulse = False
                yes = True
                engine.say('Okay we should try again')
                engine.runAndWait()
            else:
                p_pulse = False
                yes = False
    elif text == "**":
        engine.say('I did not get that')
        engine.runAndWait()
        p_pulse = False

# get pain level
while p_pain == False:
    pain()
    rec.record()
    text, c_rate = google.recognize()
    if int(round(float(c_rate)))*10 > 9:
        engine.say('You said')
        print "You said " + text
        engine.say(text)
        engine.runAndWait()
        yes = False
        while yes == False:
            engine.say('Yes or No')
            engine.runAndWait()
            rec.record()
            yn_text, c_rate = google.recognize()
            if yn_text == "yes" or yn_text == "YES" or yn_text == "Yes":
                p_pain = True
                yes = True
                pp = "pain: " + str(text) + '\n'
                file.write(pp)
            elif yn_text == "no" or yn_text == "NO" or yn_text == "No":
                p_pain = False
                yes = True
                engine.say('Okay we should try again')
                engine.runAndWait()
            else:
                p_pain = False
                yes = False
    elif text == "**":
        engine.say('I did not get that')
        engine.runAndWait()
        p_pain = False

end()
