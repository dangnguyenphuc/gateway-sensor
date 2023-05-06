import whisper
import pandas as pd
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from flask import request
from pydub import AudioSegment
import tempfile
import speech_recognition as sr
import os
import tensorflow as tf
import paho.mqtt.client as mqttclient
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split

# Load data from CSV file
df = pd.read_csv("model/Data.csv", header=None)

# Split data into train and validation sets
train_data, val_data = train_test_split(df, test_size=0.2, random_state=42)

# Convert text data to numerical data
tokenizer = Tokenizer(num_words=1000, oov_token="<OOV>")
tokenizer.fit_on_texts(train_data[0])

sess = tf.compat.v1.Session()
graph = tf.compat.v1.get_default_graph()

with sess.as_default():
    with graph.as_default():
        model = tf.keras.models.load_model("model/my_model.h5")

app = Flask(__name__)

CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

#Dang ky phia client
ADAFRUIT_USERNAME = "dangnguyen"
BROKER_ADDRESS = "io.adafruit.com"
ADAFRUIT_ACCESS_TOKEN = "aio_DsnO87BT3KLJ5mdsLQ5BS7RXp0hY"
PORT = 1883
FEED_NAME = "dangnguyen/feeds/nmdk-1-fanstatus-1"
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

@app.route('/add', methods=['POST'])
@cross_origin(origin='*')

def add_process():
    file = request.files['audio']
    if file:
        #Tải file âm thanh vào thư mục upload
        filename = file.filename
        file.save(os.path.join('upload', filename))

        # Load the audio file
        audio_path = os.path.join('upload', 'recording.m4a')
        model_1 = whisper.load_model('base.en')
        result = model_1.transcribe('upload/recording.m4a',language= 'english', fp16 = False)
        os.remove(audio_path)
        # Return the transcribed text as a response
        # Chuyển đổi đoạn văn bản mới sang chuỗi số
        text = result['text']
        new_sequences = tokenizer.texts_to_sequences([text])

        # Đệm chuỗi số với các giá trị số 0
        new_padded = pad_sequences(new_sequences, padding="post", maxlen=20)

        with sess.as_default():
            with graph.as_default():
                predictions = model.predict(new_padded)
        if predictions[0][0] > 0.5:
            aio.send(FEED_NAME,'ON')
            return 'ON'
        else: 
            aio.send(FEED_NAME,'OFF')
            return 'OFF'
    else:
        return 'No file uploaded'

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = '9999')