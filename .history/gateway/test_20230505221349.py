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
import paho.mqtt.client as mqttclient
import json
import time

ADAFRUIT_USERNAME = "dangnguyen"
BROKER_ADDRESS = "io.adafruit.com"
ADAFRUIT_ACCESS_TOKEN = "aio_VWhA64yeAJO6ui30B2ix8S8yqWEB"
PORT = 1883

feed = "dangnguyen/feeds/nmdk-1-fanstatus-1"

client = mqttclient.Client("Gateway_Adafruit")
client.username_pw_set(ADAFRUIT_USERNAME, ADAFRUIT_ACCESS_TOKEN)
client.connect(BROKER_ADDRESS, 1883)
client.publish(feed, "OFF")

df = pd.read_csv("model/Data.csv", header=None)

# Split data into train and validation sets
train_data, val_data = train_test_split(df, test_size=0.2, random_state=42)

# Convert text data to numerical data
tokenizer = Tokenizer(num_words=1000, oov_token="<OOV>")
tokenizer.fit_on_texts(train_data[0])

model = tf.keras.models.load_model("model/my_model.h5")

def play(tts):
    tts.save("Siri.wav")
    playsound.playsound('Siri.wav', True)

def record():
    global client
    tts = gTTS(text = "Xin chào, bạn hãy nói việc bạn cần làm",lang='vi')
    play(tts)
    r = sr.Recognizer()
    # Load the audio file
    with sr.Microphone() as source:
        try:
            audio = r.record(source, duration=5)
            result = r.recognize_google(audio,language="en")
            tts = gTTS(text = "Bạn đã nói:",lang='vi')
            play(tts)
            tts = gTTS(text = result,lang='en')
            play(tts)
            new_sequences = tokenizer.texts_to_sequences([result])

            # Đệm chuỗi số với các giá trị số 0
            new_padded = pad_sequences(new_sequences, padding="post", maxlen=20)

            # Dự đoán kết quả cho đoạn văn bản mới
            predictions = model.predict(new_padded)
            if predictions[0][0] > 0.5:
                client.publish(feed, "ON")
            else: 
                client.publish(feed, "OFF")
            return
        except:
            tts = gTTS(text = "Xin lỗi, tôi không hiểu hay nghe bạn nói gì",lang='vi')
            play(tts)

    return



# root window
root = tk.Tk()
root.geometry('500x500')
root.resizable(True, True)
root.title('Sound Record')


# record button
record_button = ttk.Button(
    root,
    text='Record now',
    command=record
)

record_button.pack(
    ipadx=5,
    ipady=2,
    expand=True
)

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

root.mainloop()



