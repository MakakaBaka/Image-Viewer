from PIL import Image, ImageTk
from tkinter import Tk, Label, Button
import os


def resize_image():
    global current_image
    if current_image.height > 640:
        new_width = current_image.width * (640 / current_image.height)
        current_image = current_image.resize((int(new_width), 640))
    if current_image.width > 1280:
        new_height = current_image.height * (1280 / current_image.width)
        current_image = current_image.resize((int(new_height), 1280))


def create_pic():
    global current_image
    global a
    global place_image
    resize_image()
    a = ImageTk.PhotoImage(current_image)
    place_image = Label(image=a, width=current_image.width, height=current_image.height)
    place_image.grid(row=1, column=0, columnspan=2)


def next_pic():
    global current_image
    global count
    global place_image
    place_image.grid_forget()
    count += 1
    if count == len(myfiles):
        count = 0
    current_image = Image.open('img/{x}'.format(x=myfiles[count]))
    create_pic()


def previous_pic():
    global current_image
    global count
    global place_image
    place_image.grid_forget()
    count -= 1
    if count == -1:
        count = len(myfiles) - 1
    current_image = Image.open('img/{x}'.format(x=myfiles[count]))
    create_pic()


root = Tk()
root.title('Image Viewer')
root.iconbitmap('icon.ico')

myfiles = os.listdir('img')

count = 0
current_image = Image.open('img/{x}'.format(x=myfiles[count]))

forward_button = Button(text='Forward', command=next_pic)
back_button = Button(text='Back', command=previous_pic)

forward_button.grid(row=0, column=1)
back_button.grid(row=0, column=0)

create_pic()

root.mainloop()