import tensorflow as tf 
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
import re

def no_accent_vietnamese(s):
    s = re.sub(u'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', s)
    s = re.sub(u'[ÀÁẠẢÃĂẰẮẶẲẴÂẦẤẬẨẪ]', 'A', s)
    s = re.sub(u'èéẹẻẽêềếệểễ', 'e', s)
    s = re.sub(u'ÈÉẸẺẼÊỀẾỆỂỄ', 'E', s)
    s = re.sub(u'òóọỏõôồốộổỗơờớợởỡ', 'o', s)
    s = re.sub(u'ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ', 'O', s)
    s = re.sub(u'ìíịỉĩ', 'i', s)
    s = re.sub(u'ÌÍỊỈĨ', 'I', s)
    s = re.sub(u'ùúụủũưừứựửữ', 'u', s)
    s = re.sub(u'ƯỪỨỰỬỮÙÚỤỦŨ', 'U', s)
    s = re.sub(u'ỳýỵỷỹ', 'y', s)
    s = re.sub(u'ỲÝỴỶỸ', 'Y', s)
    s = re.sub(u'Đ', 'D', s)
    s = re.sub(u'đ', 'd', s)
    return s

sentences = [
    "tôi yêu chó",
    "tôi yêu mèo"
]

sentences = [no_accent_vietnamese(sentence) for sentence in sentences]
print(sentences)
# tkenizer = Tokenizer(num_words=100)
# tkenizer.fit_on_texts(sentences)

# word_index = tkenizer.word_index
# print(word_index)

# import speech_recognition as sr 

# r = sr.Recognizer()

# with sr.Microphone() as source:
#     audio_data = r.record(source, duration=3)
#     print("Listen:")
#     text = r.recognize_google(audio_data, language="vi")
#     print(text)
