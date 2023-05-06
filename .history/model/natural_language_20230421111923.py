# import tensorflow as tf 
# from tensorflow import keras

# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences
# import re

# def no_accent_vietnamese(s):
#     s = re.sub('[áàảãạăắằẳẵặâấầẩẫậ]', 'a', s)
#     s = re.sub('[ÁÀẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬ]', 'A', s)
#     s = re.sub('[éèẻẽẹêếềểễệ]', 'e', s)
#     s = re.sub('[ÉÈẺẼẸÊẾỀỂỄỆ]', 'E', s)
#     s = re.sub('[óòỏõọôốồổỗộơớờởỡợ]', 'o', s)
#     s = re.sub('[ÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢ]', 'O', s)
#     s = re.sub('[íìỉĩị]', 'i', s)
#     s = re.sub('[ÍÌỈĨỊ]', 'I', s)
#     s = re.sub('[úùủũụưứừửữự]', 'u', s)
#     s = re.sub('[ÚÙỦŨỤƯỨỪỬỮỰ]', 'U', s)
#     s = re.sub('[ýỳỷỹỵ]', 'y', s)
#     s = re.sub('[ÝỲỶỸỴ]', 'Y', s)
#     s = re.sub('đ', 'd', s)
#     s = re.sub('Đ', 'D', s)
#     return s

# sentences = [
#     "tôi yêu chó",
#     "tôi yêu mèo"
# ]

# sentences = [no_accent_vietnamese(sentence) for sentence in sentences]
# print(sentences)

# tokenizer = Tokenizer(num_words = 100, oov_token="<OOV>")
# tokenizer.fit_on_texts(sentences)
# word_index = tokenizer.word_index

# sequences = tokenizer.texts_to_sequences(sentences)

# padded = pad_sequences(sequences, maxlen=5)
# print("\nWord Index = " , word_index)
# print("\nSequences = " , sequences)
# print("\nPadded Sequences:")
# print(padded)


# # Try with words that the tokenizer wasn't fit to
# test_data = [
#     no_accent_vietnamese('tôi rất yêu chó của tôi'),
#     no_accent_vietnamese('chó của tôi rất yêu mèo của tôi')
# ]

# test_seq = tokenizer.texts_to_sequences(test_data)
# print("\nTest Sequence = ", test_seq)

# padded = pad_sequences(test_seq, maxlen=10)
# print("\nPadded Test Sequence: ")
# print(padded)

import speech_recognition as sr 

r = sr.Recognizer()

with sr.Microphone() as source:
    audio_data = r.record(source, duration=3)
    print("Listen:")
    text = r.recognize_google(audio_data, language="vi", show_all = True)
    print(text)


# import openai

# openai.api_key = "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"

# output = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     message=[{
#         "role":"user",
#         "content": "Hello, how are you?"
#     }]
# )

# print(output)

# import speech_recognition as sr
# import spacy

# # load the pre-trained Vietnamese language model
# nlp = spacy.load("xx_ent_wiki_sm") # or "vi_core_news_sm"

# # obtain audio from the microphone
# r = sr.Recognizer()
# with sr.Microphone() as source:
#     audio_data = r.record(source, duration=3)
#     print("Say something!")
#     text = r.recognize_google(audio_data, language="vi", show_all = True)
#     print(text)

# recognize speech using Google Speech Recognition


# # process the text with spaCy
# doc = nlp(text)

# # extract the numerical value using NER
# for ent in doc.ents:
#     if ent.label_ == "CARDINAL":
#         print(ent.text)