import datetime # for datetime
# import speech module for taking microphone input as 'SRG'
import speech_recognition as SRG
#For speak function
from win32com.client import Dispatch #import dispatch for speak function
# for results from wikipedia
import wikipedia

# Speak function
def speak(s):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(s)


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good morning")
        speak("Good morning")
    elif hour>=12 and hour<18:
        print("Good afternoon")
        speak("Good afternoon")
    else:
        print("Good evening")
        speak("Good evening")
    print("I am safi. The AI assistant. How may i assist you??")
    speak("I am safi. The AI assistant. How may i assist you??")

# function for taking microphone input
def take_command():
    store = SRG.Recognizer()
    with SRG.Microphone() as s:
        print("Listening...")
        audio_input = store.record(s, duration=3)
        try:
            text_output = store.recognize_google(audio_input)
            print("User said : ",text_output)
        except:
            print("Say that again please...")
            return "None"
    return text_output
if __name__ == '__main__':
    wish_me()
    while(True):
        query=take_command().lower()
        #logic for executing tasks
        if "stop" in query:
            break
