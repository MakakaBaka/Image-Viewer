from PIL import Image, ImageTk
from tkinter import Tk, Label, Button
import os


myfiles = os.listdir('img')
print(myfiles)

def create_pic():
    global current_image
    global a
    global place_image
    if current_image.height > 640:
        new_width = current_image.width * (640 / current_image.height)
        a = ImageTk.PhotoImage(current_image.resize((int(new_width), 640)))
    else:
        a = ImageTk.PhotoImage(current_image)
    place_image = Label(image=a)
    place_image.grid(row=1, column=0, columnspan=3)

def next_pic():
    global current_image
    global y
    y += 1
    if y == 7:
        y = 1
    current_image = Image.open('img/{x}.jpg'.format(x=y))
    create_pic()

def previous_pic():
    global current_image
    global y
    y -= 1
    if y == 0:
        y = 6
    current_image = Image.open('img/{x}.jpg'.format(x=y))
    create_pic()

root = Tk()

current_image = Image.open('img/1.jpg')
y = 1

create_pic()

forward_button = Button(text='Forward', command=next_pic)
back_button = Button(text='Back', command=previous_pic)

forward_button.grid(row=0, column=2)
back_button.grid(row=0, column=0)


root.mainloop()