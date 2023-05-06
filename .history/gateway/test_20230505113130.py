from gtts import gTTS
import os
import playsound
import tkinter as tk
from tkinter import ttk
import speech_recognition as sr
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

df = pd.read_csv("model/Data.csv", header=None)

# Split data into train and validation sets
train_data, val_data = train_test_split(df, test_size=0.2, random_state=42)

# Convert text data to numerical data
tokenizer = Tokenizer(num_words=1000, oov_token="<OOV>")
tokenizer.fit_on_texts(train_data[0])

def play(tts):
    tts.save("Siri.wav")
    playsound.playsound('Siri.wav', True)

def record():
    tts = gTTS(text = "Xin chào, bạn hãy nói việc bạn cần làm",lang='vi')
    play(tts)
    r = sr.Recognizer()
    # Load the audio file
    with sr.Microphone() as source:
        audio = r.record(source, duration=3)
        result = r.recognize_google(audio,language="en")
        tts = gTTS(text = "Bạn đã nói:",lang='vi')
        tts = gTTS(text = result,lang='en')
        play(tts)
        return
    return



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

record_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

root.mainloop()



