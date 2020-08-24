from PIL import Image, ImageTk
from tkinter import Tk, Label, Button
import os
from tkinter import filedialog, messagebox


def choose_pic():
    place_image.grid_forget()
    path_to_file = filedialog.askopenfilename(title='Choose file',
                                          filetypes=(('all files', '*.*'), ('png files', '*.png'), ('JPEG files', '*.jpg'))
                                          )
    try:
        pic = Image.open(path_to_file)
        create_pic(pic)
        change_dir(path_to_file)
    except OSError:
        messagebox.showerror("Error", "Unsupported file type")
        choose_pic()
    except AttributeError:
        print('de kartinka? (((')


def change_dir(path):
    global myfiles, directory, count
    directory = os.path.dirname(path)
    myfiles = os.listdir(directory)
    filename = os.path.basename(path)
    count = myfiles.index(filename)


def resize_image(image):
    # Measuring screen resolution and subtracting some numbers for better fitting of images
    screen_width = root.winfo_screenwidth() - 50
    screen_height = root.winfo_screenheight() - 100
    if image.height > screen_height:
        new_height = screen_height
        new_width = image.width * (screen_height / image.height)
        image = image.resize((int(new_width), new_height))
    if image.width > screen_width:
        new_width = screen_width
        new_height = image.height * (screen_width / image.width)
        image = image.resize((new_width, int(new_height)))
    return image


# Tkinter decided that 'image_ready' should be global for it`s own reasons
def create_pic(image):
    global place_image, image_ready
    place_image.grid_forget()
    image = resize_image(image)
    image_ready = ImageTk.PhotoImage(image)
    place_image = Label(image=image_ready, width=image.width, height=image.height)
    place_image.grid(row=1, column=0, columnspan=3)


def next_pic():
    global count
    place_image.grid_forget()
    count += 1
    if count == len(myfiles):
        count = 0
    try:
        image = Image.open('{dir}/{x}'.format(dir=directory, x=myfiles[count]))
        create_pic(image)
    except OSError:
        next_pic()


def previous_pic():
    global count
    place_image.grid_forget()
    count -= 1
    if count == -1:
        count = len(myfiles) - 1
    try:
        image = Image.open('{dir}/{x}'.format(dir=directory, x=myfiles[count]))
        create_pic(image)
    except OSError:
        previous_pic()


root = Tk()
root.title('Image Viewer')
root.iconbitmap('icon.ico')

myfiles = os.listdir('sample_img')
directory = 'sample_img'
count = 0

starting_image = Image.open('sample_img/{x}'.format(x=myfiles[count]))
starting_image_ready = ImageTk.PhotoImage(starting_image)
place_image = Label(image=starting_image_ready, width=starting_image.width, height=starting_image.height)
place_image.grid(row=1, column=0, columnspan=3)

forward_button = Button(text='Forward', command=next_pic)
back_button = Button(text='Back', command=previous_pic)
choose_button = Button(text='Open picture', command=choose_pic)

forward_button.grid(row=0, column=2)
back_button.grid(row=0, column=0)
choose_button.grid(row=0, column=1)

root.mainloop()
