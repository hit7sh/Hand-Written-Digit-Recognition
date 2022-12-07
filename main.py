from tkinter import *
# import tensorflow as tf
from PIL import ImageGrab
import numpy as np
# import cv2
import time
# from keras.models import load_model
# import matplotlib


# matplotlib.use('Agg')

window = Tk()
window.title("Digit Recognition")

window.state("zoomed")
window.resizable(False, False)
window['bg'] = '#ffe8a8'

# create canvas
wn = Canvas(window, width=280, height=280, bg='black')

txt = Label(text='Please Write a digit...', font=(
    'consolas', 50, 'bold'), fg='green')
txt.pack(side=BOTTOM)

# model = load_model('digitrec2.h5')

pen_size = 10

slider = Scale(window, from_=4, to=15, orient=HORIZONTAL, font=(
    'consolas', 20, 'bold'))
slider.set(10)
slider.place(x=800, y=100)


def paint(event):
    pen_size = slider.get()
    # get x1, y1, x2, y2 co-ordinates
    x1, y1 = (event.x-pen_size), (event.y-pen_size)
    x2, y2 = (event.x+pen_size), (event.y+pen_size)
    color = "#c6c9f5"
    # display the mouse movement inside canvas
    wn.create_oval(x1, y1, x2, y2, fill=color, outline=color)


def showtext(st):
    txt['text'] = st


def clear():
    wn.delete("all")
    showtext('Please write a digit...')


def capture():
    im = ImageGrab.grab((750, 40, 1170, 455))
    return im


def predict():
    # showtext('predicting...')
    # image = capture()
    # image.save('photo.png')
    # img = cv2.imread('photo.png')
    # # image.show()
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # resized = cv2.resize(gray, (28, 28))
    # nimg = tf.keras.utils.normalize(resized, axis=1)
    # nimg = np.array(nimg).reshape(1, 28, 28, 1)
    # ans = np.argmax(model.predict(nimg))

    showtext(f'You wrote a 🧐💭')


btn = Button(text='clear🗑', command=clear, font=(
    'consolas', 20, 'bold'), bg='gold')
btn.place(x=500, y=300)
# btn.pack(side=LEFT)

btn1 = Button(text='predict', font=('consolas', 20, 'bold'),
              command=predict, bg='gold')
btn1.place(x=650, y=300)
# btn1.pack(side=RIGHT)

# bind mouse event with canvas(wn)
wn.bind('<B1-Motion>', paint)
wn.pack()
window.mainloop()

# img = cv2.imread('number1.png')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# resized = cv2.resize(gray, (28, 28))
# nimg = tf.keras.utils.normalize(resized, axis=1)
# nimg = np.array(nimg).reshape(1, 28, 28, 1)
# print(np.argmax(model.predict(nimg)))
