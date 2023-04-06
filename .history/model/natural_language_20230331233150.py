# import tensorflow as tf 
# from tensorflow import keras
# from tensorflow.keras.preprocessing.text import Tokenizer

# sentences = [
#     "toi yeu mina",
#     "toi yeu yen"
# ]

# tkenizer = Tokenizer(num_words=100)
# tkenizer.fit_on_texts(sentences)

# word_index = tkenizer.word_index
# print(word_index)


import speech_recognition as sr

# create a recognizer object
r = sr.Recognizer()

# use the default microphone as the audio source
with sr.Microphone() as source:
    print("Speak something...")
    # listen for audio and convert it to text
    audio = r.listen(source)
# recognize speech using Google Speech Recognition
try:
    text = r.recognize_google(audio)
    print("You said: " + text)
except sr.UnknownValueError:
    print("Sorry, could not understand audio.")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
