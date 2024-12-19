
import pyfirmata
import speech_recognition as sr
import datetime
import time



def word_to_number(word):
    word_map = {
        "zero": "0", "one": "1", "two": "2", "three": "3", 
        "four": "4", "five": "5", "six": "6", "seven": "7", 
        "eight": "8", "nine": "9", "ten": "10"
    }
    return word_map.get(word.lower(), word)

def listen():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 0.8
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(query)
            
        except Exception as e:
            print(e)
            print("Say that again please...")
            return "None"
        query = query.lower()
        return query



try:
    board = pyfirmata.Arduino('COM7')
    board.digital[6].mode = pyfirmata.OUTPUT
    board.digital[6].write(0)
   

except Exception as a:
    print("arduino not connected")

while True:

    query = listen()

    

    if "turn on the lamp for" in query:
        query = query.replace("turn on the lamp for","")
        query = query.replace("seconds","")
        query = word_to_number(query)
        board.digital[6].write(1)
        time.sleep(int(query))
        board.digital[6].write(0)

    elif "turn off the lamp after" in query:
        query = query.replace("turn off the lamp after","")
        query = query.replace("seconds","")
        query = word_to_number(query)
        board.digital[6].write(1)
        time.sleep(int(query))
        board.digital[6].write(0)

    elif "turn on" in query or "switch on" in query:
        board.digital[6].write(1)


    elif "turn off" in query or "switch off" in query:
        board.digital[6].write(0)


    else:
        pass

