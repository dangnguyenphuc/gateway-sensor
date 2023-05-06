from gtts import gTTS
import os
import playsound

tts = gTTS(text = "Xin chào",lang='vi')

def play(tts):
    tts.save("Siri.mp3")
    playsound.playsound('Siri.mp3', True)




