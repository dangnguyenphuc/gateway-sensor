from gtts import gTTS
import os
import playsound
import tkinter as tk
from tkinterimport speech_recognition as sr


def play(tts):
    tts.save("Siri.wav")
    playsound.playsound('Siri.wav', True)

tts = gTTS(text = "Xin chào",lang='vi')



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
    ipady=5,
    expand=True
)
play(tts)
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

