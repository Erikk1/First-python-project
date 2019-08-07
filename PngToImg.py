import os
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog
from PIL import Image


root = Tk()
root.geometry("700x100")
root.title("Image Converter")
menu = Menu(root)
root.config(menu=menu)
subMenu = Menu(menu)

def browse_file():
    global im
    global filename
    filename = filedialog.askopenfilename()
    im = Image.open(fp=filename)
    statusbar['text']=">>> Chosen image: " + '' + os.path.basename(filename)


def save():
    global im
    files = [('All files', '*.*'),
             ('.jpeg', '*.py'),
             ('Text Document', '*.txt')]
    im = im.convert("RGB")  #
    save_filename = filedialog.asksaveasfile(filetypes=files, defaultextension=files)
    im.save(save_filename)

def loe_mind():
    tkinter.messagebox.showinfo('Selgitus:',
                                'See programm konverdib Teie .png pildi .jpg pildiks, lihtsalt lisage konverditud pildi'
                                'nime lõppu ".jpg" ')

menu.add_cascade(label="Info",menu=subMenu)
subMenu.add_command(label="Loe mind!", command=loe_mind)

leftframe = Frame(root)
leftframe.pack(side=LEFT, padx=30)

rightframe = Frame(root)
rightframe.pack(side=RIGHT, padx=30)

Lisa_fail = Button(leftframe, text="Add image", command=browse_file)
Lisa_fail.pack()

ConvertNupp = Button(rightframe, text="Convert and save image", command=save)
ConvertNupp.pack()

statusbar = Label(root, text='>Image name comes here<', relief=SUNKEN,anchor=W)
statusbar.pack(side=BOTTOM, fill=X)







def sulgemine():
    root.destroy()
root.protocol("WM_DELETE_WINDOW", sulgemine)

root.mainloop()