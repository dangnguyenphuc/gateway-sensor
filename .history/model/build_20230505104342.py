# import pandas as pd
# import tensorflow as tf
# from sklearn.model_selection import train_test_split
# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences

# # Load data from CSV file
# df = pd.read_csv("model/Data.csv")
# data = df["text"]
# lable = df["lable"]


# # Split data into train and validation sets
# train_data, val_data = train_test_split(df, test_size=0.2, random_state=42)

# train_text = train_data["text"]
# train_lable = train_data["lable"]

# test_text = val_data["text"]
# test_lable = val_data["lable"]



# # Convert text data to numerical data
# tokenizer = Tokenizer(num_words=1000, oov_token="<OOV>")
# tokenizer.fit_on_texts(train_text)

# train_sequences = tokenizer.texts_to_sequences(train_text)
# train_padded = pad_sequences(train_sequences, padding="post", maxlen=20)

# val_sequences = tokenizer.texts_to_sequences(test_text)
# val_padded = pad_sequences(val_sequences, padding="post", maxlen=20)

# # Define the model
# model = tf.keras.Sequential([
#     tf.keras.layers.Embedding(input_dim=1000, output_dim=16, input_length=20),
#     tf.keras.layers.GlobalAveragePooling1D(),
#     tf.keras.layers.Dense(16, activation="relu"),
#     tf.keras.layers.Dense(1, activation="sigmoid")
# ])

# # Define loss function and optimizer
# model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

# # Train the model
# hítory = model.fit(train_padded, train_lable, epochs=60, validation_data=(val_padded, test_lable))

# # Evaluate the model
# model.evaluate(val_padded, test_lable)

# # model.save("my_model.h5")

# # # Chuỗi văn bản mới cần được dự đoán
# text = "turn on the light"

# # Chuyển đổi đoạn văn bản mới sang chuỗi số
# new_sequences = tokenizer.texts_to_sequences([text])

# # Đệm chuỗi số với các giá trị số 0
# new_padded = pad_sequences(new_sequences, padding="post", maxlen=20)

# # # Dự đoán kết quả cho đoạn văn bản mới
# predictions = model.predict(new_padded)

# # # In kết quả
# print("Dang")
# print(predictions)

import pandas as pd
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Embedding, Flatten, Dense

# Load data into a pandas DataFrame
data = pd.read_csv('model/Data.csv')

# Preprocess text data
tokenizer = Tokenizer(num_words=5000)
tokenizer.fit_on_texts(data['text'])
X = tokenizer.texts_to_sequences(data['text'])
X = pad_sequences(X, maxlen=100)

# Preprocess label data
y = data['label']




# Define Keras model
model = Sequential()
model.add(Embedding(5000, 100, input_length=100))
model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(3, activation='sigmoid'))

# Compile Keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X, y, epochs=10, batch_size=32, validation_split=0.2)