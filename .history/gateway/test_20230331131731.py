from gtts import gTTS
import os
import soundfile
import librosa
import matplotlib.pyplot as plt
import numpy as np
import math

file_path = r'example.mp3'
#
#
signal, sr = librosa.load(file_path, sr = 16000)
# plt.plot(signal)
#
RMS=math.sqrt(np.mean(signal**2))

STD_n= 0.001
noise=np.random.normal(0, STD_n, signal.shape[0])
#
# # X=np.fft.rfft(noise)
# # radius,angle=to_polar(X)
#
signal_noise = signal+noise

soundfile.write('example.mp3',signal_noise,16000)
os.system("ffplay example.mp3")