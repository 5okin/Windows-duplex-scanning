import os
import tkinter
import time
from tkinter import *
from tkinter import filedialog
from natsort import natsorted, natsort_keygen
from pathlib import Path
from PIL import Image


class HoverButton(tkinter.Button):
    def __init__(self, master, **kw):
        tkinter.Button.__init__(self, master=master, **kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground


def create_pdf():
    print(create_pdf.get())
    print('hi')


def directory_browse():
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    dir_textbox.delete(0, END)
    dir_textbox.insert(10, folder_path.get())
    dir_textbox.xview_moveto(1)


def focus_newdir_tb(event):
    if new_dir_textbox.get() == "(Optional)":
        new_dir_textbox.delete(0, "end")
        new_dir_textbox['foreground'] = 'black'
    return None


def unfocus_newdir_tb(event):
    if not new_dir_textbox.get():
        new_dir_textbox.delete(0, "end")
        new_dir_textbox.insert(0, "(Optional)")
        new_dir_textbox['foreground'] = 'grey'
    return None


def sorting_preparation():

    '''
    if create_pdf.get():
        print(create_pdf.get())
    '''

    dir = dir_textbox.get()
    page = (int(pagesNumTextBox.get())+1)
    LastFS = ("Image (" + str(page) + ").jpg")

    # Check if user wants to create a new dir and move arranged document there
    DestinationPath = dir_textbox.get()
    if new_dir_textbox.get() != "(Optional)":
        DestinationPath = os.path.join(DestinationPath, new_dir_textbox.get())

        if not os.path.exists(DestinationPath):
            os.makedirs(DestinationPath)


    FirstScan = ("Image.jpg" in natsorted(os.listdir(dir)))
    if (FirstScan is True):
        os.rename(os.path.join(dir, "Image.jpg"), os.path.join(dir, "Image (1).jpg"))

    SplitPoint = (natsorted(os.listdir(dir))).index(LastFS)
    Front = ((natsorted(os.listdir(dir)))[0:SplitPoint])
    Rear = ((natsorted(os.listdir(dir)))[SplitPoint:])

    i = 1
    for file in Front:
        name = ("Scan (" + str(i) + ").jpg")
        if file.endswith(".jpg"):
            old_opj = (os.path.join(dir, file))
            new_opj = (os.path.join(DestinationPath, name))
            os.rename(old_opj, new_opj)
            i += 2

    natsort_key = natsort_keygen()

    i = 2
    for file in sorted(Rear, key=natsort_key, reverse=True):
        name = ("Scan (" + str(i) + ").jpg")
        if file.endswith(".jpg"):

            old_opj = (os.path.join(dir, file))
            new_opj = (os.path.join(DestinationPath, name))
            os.rename(old_opj, new_opj)
            i += 2

    images = Path(DestinationPath).glob("*.jpg")
    image_strings = [str(p) for p in images]
    image_strings = sorted(image_strings, key=natsort_key, reverse=False)

    if create_pdf.get():
        images = [
            Image.open(img)
            for img in image_strings
        ]

        filename = f'scan_{time.strftime("%Y_%m_%d-%H_%M_%S")}.pdf'

        images[0].save(
            os.path.join(DestinationPath, filename), "PDF", resolution=100.0, save_all=True, append_images=images[1:]
        )

        images = Path(DestinationPath).glob("*.jpg")
        image_strings = [str(p) for p in images]
        image_strings = sorted(image_strings, key=natsort_key, reverse=False)

    if not keep_images.get():
        for img in image_strings:
            if os.path.exists(img):
                os.remove(img)

root = Tk()
root.resizable(False, False)
root.configure(bg='#1E1F22')
create_pdf = tkinter.IntVar(value=0)
keep_images = tkinter.IntVar(value=1)
#root.geometry("400x120")
#root.iconbitmap(default='Blank.ico')
root.title("Duplex Scanning")

sel = IntVar()
folder_path = StringVar()

folder_path.set(os.path.dirname(os.path.realpath(__file__)))

Label(root, text="Directory", bg='#1E1F22', fg='white').grid(row=0)
Label(root, text="Number of pages", bg='#1E1F22', fg='white').grid(row=1, column=0)
Label(root, text="New folder name", bg='#1E1F22', fg='white').grid(row=3)
#Label(root, text="Merge to PDF", bg='#1E1F22', fg='white').grid(row=4)
#Label(root, text="Keep original images", bg='#1E1F22', fg='white').grid(row=4, column=2)


button2 = HoverButton(root, text="Browse", command=directory_browse, bg='#305FB9', fg='white',
                      highlightthickness=2, highlightbackground ='white', bd=0,
                      activebackground='#25498e', activeforeground='white')

button1 = HoverButton(root, text=' Ok ', command=sorting_preparation, bg='#2EA043', fg='white',
                      activebackground="#238636", activeforeground='white')

pdfcheck = Checkbutton(root,
                       text="Merge to PDF",
                       variable=create_pdf,
                       onvalue=True, offvalue=False,
                       #command=create_pdf,
                       bg='#1E1F22', fg='white',
                       activebackground='#1E1F22', activeforeground='white',
                       selectcolor='black')

keepog = Checkbutton(root,
                     text="Keep original images",
                     variable=keep_images,
                     onvalue=True, offvalue=False, bg='#1E1F22', fg='white',
                     activebackground='#1E1F22', activeforeground='white',
                     selectcolor='black')

dir_textbox = Entry(root, bg='#e4e5e7')
pagesNumTextBox = Spinbox(root, from_=2, to=9999999, bg='#e4e5e7')
new_dir_textbox = Entry(root, fg='grey', bg='#e4e5e7')

dir_textbox.insert(10, folder_path.get())
dir_textbox.xview_moveto(1)                              # Set alignment to right side

new_dir_textbox.insert(0, "(Optional)")

new_dir_textbox.bind("<FocusIn>", focus_newdir_tb)
new_dir_textbox.bind("<FocusOut>", unfocus_newdir_tb)

# GUI alignment
dir_textbox.grid(row=0, sticky=W+E, column=1, pady=5, padx=5)
pagesNumTextBox.grid(row=1, column=1, sticky=W+E, columnspan=3, pady=5, padx=5)
new_dir_textbox.grid(row=3, column=1, sticky=W+E, columnspan=3, pady=5, padx=5)
pdfcheck.grid(row=4, column=0, sticky=W)
keepog.grid(row=4, column=1, sticky=W)
button2.grid(row=0, column=3, pady=2, padx=5)
button1.grid(row=5, sticky=N+S+E+W, columnspan=4,  pady=5, padx=5)

mainloop()
