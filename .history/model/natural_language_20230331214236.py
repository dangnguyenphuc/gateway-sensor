import tensorflow as tf 
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer

sentences = [
    "toi yeu mina",
    "toi yeu yen"
]

tkenizer = Tokenizer(num_words=100)
