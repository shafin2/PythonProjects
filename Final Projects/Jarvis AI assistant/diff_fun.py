import speech_recognition as sr
from datetime import datetime
def take_input():
    time_start=datetime.now().strftime('%S')
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 100
        r.adjust_for_ambient_noise(source)
        print("say anything : ")
        audio = r.listen(source)
        time_end=datetime.now().strftime('%S')
        if int(time_end)-int(time_start)<2:
            text = r.recognize_google(audio)
            print(audio)
        else:
            print("sorry, could not recognise Say again")
            take_input()


if __name__ == '__main__':
    while(True):
        take_input()




























#
#
# import speech_recognition as SRG
# import time
#
# store = SRG.Recognizer()
# with SRG.Microphone() as s:
#     print("Speak...")
#
#     audio_input = store.record(s, duration=4)
#     print("Recording time:", time.strftime("%I:%M:%S"))
#
#     try:
#         text_output = store.recognize_google(audio_input)
#         print("Text converted from audio:\n")
#         print(text_output)
#
#         print("Execution time:", time.strftime("%I:%M:%S"))
#     except:
#         print("Couldn't process the audio input.")