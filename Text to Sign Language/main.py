import numpy as np
import matplotlib.pyplot as plt
from easygui import *
from PIL import Image, ImageTk
from itertools import count
import tkinter as tk
import string

def display_sign_language(text):
    isl_gif = ['any questions','be careful', 'did you book tickets', 'good afternoon', 'good evening', 'good morning', 'good night',
               'good question', 'happy journey', 'hello what is your name', 'i am sorry', 'i am thinking', 'i love to shop', 'i had to say something but I forgot', 'i have headache', 'i like pink colour','i live in nagpur', 
               'nice to meet you','no smoking please', 'please wait for sometime','shall I help you', 'shall we go together tomorrow', 'sign language interpreter', 'take care', 'what is the problem', 'what is today\'s date', 
               'what is your mobile number','what is your name', 'address', 'agra', 'ahmedabad', 'assam', 'august', 'australia', 'baroda', 'banaras', 'bangalore', 'bihar', 
               'cat', 'chandigarh', 'chennai', 'church', 'delhi', 'hello', 'hyderabad', 'india', 'karnataka', 'kerala','mile', 'mumbai', 'nagpur', 'pakistan', 'punjab', 'rajasthan', 'tamil nadu', 'town', 'tuesday', 
               'please wait for sometime', 'what is your mobile number', 'what are you doing',]
    
    arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    text = text.lower()
    for c in string.punctuation:
        text = text.replace(c, "")

    if text == 'goodbye' or text == 'good bye' or text == 'bye':
        print("Oops! Time to say goodbye")
        return

    elif text in isl_gif:
        class ImageLabel(tk.Label):
            def load(self, im):
                if isinstance(im, str):
                    im = Image.open(im)
                self.loc = 0
                self.frames = []

                try:
                    for i in count(1):
                        self.frames.append(ImageTk.PhotoImage(im.copy()))
                        im.seek(i)
                except EOFError:
                    pass

                try:
                    self.delay = im.info['duration']
                except:
                    self.delay = 100

                if len(self.frames) == 1:
                    self.config(image=self.frames[0])
                else:
                    self.next_frame()

            def unload(self):
                self.config(image=None)
                self.frames = None

            def next_frame(self):
                if self.frames:
                    self.loc += 1
                    self.loc %= len(self.frames)
                    self.config(image=self.frames[self.loc])
                    self.after(self.delay, self.next_frame)

        root = tk.Tk()
        lbl = ImageLabel(root)
        lbl.pack()
        lbl.load(f'ISL_Gifs/{text}.gif')
        root.mainloop()

    else:
        for char in text:
            if char in arr:
                ImageAddress = f'letters/{char}.jpg'
                ImageItself = Image.open(ImageAddress)
                ImageNumpyFormat = np.asarray(ImageItself)
                plt.imshow(ImageNumpyFormat)
                plt.draw()
                plt.pause(0.5)
            else:
                continue

while True:
    text_input = enterbox("Enter text for sign language conversion:", "Text to Sign Language")

    if text_input is None:
        # User closed the input dialog
        break

    display_sign_language(text_input)
    plt.close()