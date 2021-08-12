import os
from tkinter import *
from tkinter import filedialog
from natsort import natsorted, natsort_keygen


def directory_browse():
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    dir_textbox.delete(0, END)
    dir_textbox.insert(10,folder_path.get())
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


def sorting_peration():
    dir = dir_textbox.get()
    page = (int(pagesNumTextBox.get())+1)
    LastFS = ("Image (" + str(page) + ").jpg")

    # Check if user wants to create a new dir and move arranged document there
    DestinationPath = dir_textbox.get()
    if new_dir_textbox.get() != "(Optional)":
        DestinationPath = os.path.join(DestinationPath, new_dir_textbox.get())

        if not os.path.exists(DestinationPath):
            os.makedirs(DestinationPath)

    #print (natsorted(os.listdir(dir)))

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
            i+=2

    natsort_key = natsort_keygen()

    i = 2
    for file in sorted(Rear, key=natsort_key, reverse=True):
        name = ("Scan (" + str(i) + ").jpg")
        if file.endswith(".jpg"):
            old_opj = (os.path.join(dir, file))
            new_opj = (os.path.join(DestinationPath, name))
            os.rename(old_opj, new_opj)
            i+=2

root = Tk()
root.resizable(False, False)
root.geometry("400x120")
#root.iconbitmap(default='Blank.ico')
root.title("Dublex Scanning")

sel = IntVar()
folder_path = StringVar()

folder_path.set(os.path.dirname(os.path.realpath(__file__)))

Label(root, text="Directory").grid(row=0)
Label(root, text="Number of pages").grid(row=1, column=0)
Label(root, text = "New folder name").grid (row=3)

button2 = Button(text="Browse", command=directory_browse)
button1 = Button(root, text=' Ok ', command=sorting_peration)

dir_textbox = Entry(root)
pagesNumTextBox = Spinbox(root, from_=3, to=9999999)
new_dir_textbox = Entry(root, fg='grey')

dir_textbox.insert(10,folder_path.get())
dir_textbox.xview_moveto(1)                              # Set alignment to right side

new_dir_textbox.insert(0, "(Optional)")

new_dir_textbox.bind("<FocusIn>", focus_newdir_tb)
new_dir_textbox.bind("<FocusOut>", unfocus_newdir_tb)

# GUI alignment
dir_textbox.grid(row=0, column=1)
pagesNumTextBox.grid(row=1, column=1)
new_dir_textbox.grid(row=3, column=1, columnspan=2)
button1.grid(row=4, column=1, sticky=S, pady=4)
button2.grid(row=0, column=3)

mainloop( )
