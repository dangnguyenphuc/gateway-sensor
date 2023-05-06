from gtts import gTTS
import os
import playsound
import tkinter as tk
from tkinter import ttk



def play(tts):
    tts.save("Siri.mp3")
    playsound.playsound('Siri.mp3', True)

tts = gTTS(text = "Xin chào",lang='vi')

play(tts)

# root window
root = tk.Tk()
root.geometry('500x500')
root.resizable(True, True)
root.title('Button Demo')

# exit button
exit_button = ttk.Button(
    root,
    text='Exit',
    command=lambda: root.quit()
)

exit_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

root.mainloop()