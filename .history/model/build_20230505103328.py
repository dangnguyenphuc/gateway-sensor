import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load data from CSV file
df = pd.read_csv("model/Data.csv")
data = df["text"]
lable = df["lable"]


# Split data into train and validation sets
train_data, val_data = train_test_split(df, test_size=0.2, random_state=42)
train_text = train_data["text"]

# # Convert text data to numerical data
# tokenizer = Tokenizer(num_words=1000, oov_token="<OOV>")
# tokenizer.fit_on_texts(train_data[0])
# train_sequences = tokenizer.texts_to_sequences(train_data[0])
# train_padded = pad_sequences(train_sequences, padding="post", maxlen=20)
# val_sequences = tokenizer.texts_to_sequences(val_data[0])
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
# hítory = model.fit(train_padded, train_data[1], epochs=50, validation_data=(val_padded, val_data[1]))

# # Evaluate the model
# model.evaluate(val_padded, val_data[1])

# model.save("my_model.h5")

# # Chuỗi văn bản mới cần được dự đoán
# text = "turn on the light"

# # Sử dụng cùng một Tokenizer đã sử dụng trước đó
# tokenizer = Tokenizer(num_words=1000, oov_token="<OOV>")
# tokenizer.fit_on_texts(train_data[0])

# # Chuyển đổi đoạn văn bản mới sang chuỗi số
# new_sequences = tokenizer.texts_to_sequences([text])

# # Đệm chuỗi số với các giá trị số 0
# new_padded = pad_sequences(new_sequences, padding="post", maxlen=20)

# # Dự đoán kết quả cho đoạn văn bản mới
# predictions = model.predict(new_padded)

# # In kết quả
# print(predictions)