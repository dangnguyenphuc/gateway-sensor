from gtts import gTTS
import os
import playsound
import tkinter as tk
from tkinter import ttk
import speech_recognition as sr


def play(tts):
    tts.save("Siri.wav")
    playsound.playsound('Siri.wav', True)

def record():
    tts = gTTS(text = "Xin chào, bạn hãy nói việc bạn cần làm",lang='vi')
    play(tts)




# root window
root = tk.Tk()
root.geometry('500x500')
root.resizable(True, True)
root.title('Sound Record')


# exit button
exit_button = ttk.Button(
    root,
    text='Exit',
    command=lambda: root.quit()
)

exit_button.pack(
    ipadx=5,
    ipady=2,
    expand=True
)

# record button
record_button = ttk.Button(
    root,
    text='Record now',
    command=record
)

record__button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

root.mainloop()



# Initialize a new recognizer instance
r = sr.Recognizer()

# Load the audio file
with sr.Microphone() as source:
    audio = r.record(source, duration=3)
    print("Speak now...")
    result = r.recognize_google(audio,language="en")
    print(result)
    # Print the recognized text and the start and end times for each phrase
    # Print the recognized text and the start and end times for each phrase 

