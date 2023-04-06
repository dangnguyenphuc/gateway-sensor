from gtts import gTTS
import os
import soundfile

mytext = "Hi, this is an example of converting text to audio. This is a bot speaking here, not a real human!"
audio = gTTS(text=mytext, lang="en", slow=False)
audio.save("example.mp3")
soundfile.write('example.mp3',signal_noise,16000)
os.system("ffplay example.mp3")