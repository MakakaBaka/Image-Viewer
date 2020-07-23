from PIL import Image, ImageTk
from tkinter import Tk, Label, Button
import os


myfiles = os.listdir('img')
print(myfiles)

def resize_image():
    global current_image
    if current_image.height > 640:
        new_width = current_image.width * (640 / current_image.height)
        current_image = current_image.resize((int(new_width), 640))
    if current_image.width > 1280:
        new_height = current_image.height * (1280 / current_image.width)
        current_image = current_image.resize((int(new_height), 1280))
#    root.geometry(str(current_image.width) + 'x' + str(current_image.height+20))

def create_pic():
    global current_image
    global a
    resize_image()
    a = ImageTk.PhotoImage(current_image)
    place_image = Label(image=a, width=current_image.width, height=current_image.height)
    place_image.grid(row=1, column=0, columnspan=2)
    forward_button.grid(row=0, column=1)
    back_button.grid(row=0, column=0)


def next_pic():
    global current_image
    global count
    count += 1
    if count == len(myfiles):
        count = 0
    current_image = Image.open('img/{x}'.format(x=myfiles[count]))
    create_pic()

def previous_pic():
    global current_image
    global count
    count -= 1
    if count == -1:
        count = len(myfiles) - 1
    current_image = Image.open('img/{x}'.format(x=myfiles[count]))
    create_pic()

root = Tk()

count = 0
current_image = Image.open('img/{x}'.format(x=myfiles[count]))

forward_button = Button(text='Forward', command=next_pic)
back_button = Button(text='Back', command=previous_pic)

create_pic()

root.mainloop()