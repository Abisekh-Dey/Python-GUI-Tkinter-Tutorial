from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

root=Tk()
root.geometry("640x700")
root.minsize(380,200)
root.configure(bg="white")
root.title("Untitled - Notepad")

text=Text(root,font="arial 12")
text.pack(fill=BOTH,expand=True)
sbar=Scrollbar(text,orient="vertical",width=20,highlightbackground="black")
sbar.pack(fill=Y,side=RIGHT)
text.config(yscrollcommand=sbar.set)
sbar.config(command=text.yview)
file=None

#File Menu
def new_tab():
    global file
    file=None
    text.delete(1.0,END)

def new_window():
    pass

def open_file():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All files","*.*"),("Text Documeents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+" - Notepad")
        text.delete(1.0,END)
        f=open(file,"r")
        text.insert(1.0,f.read())
        f.close()

def save():
    global file
    if file==None:
        file=asksaveasfilename(initialfile = 'Untitled.txt',defaultextension=".txt",filetypes=[("All files","*.*"),("Text Documents","*.txt")])
        if file=="":
            file=None
        else:
            f=open(file,"w")
            f.write(text.get(1.0,END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
            

    else:
        f=open(file,"w")
        f.write(text.get(1.0,END))
        f.close()

def save_as():
    pass

def save_all():
    pass

def page_setup():
    pass

def print():
    pass

def close_tab():
    pass

def close_window():
    pass

def exit():
    root.destroy()

menus=Menu(root)
filem=Menu(menus,tearoff=0)
filem.add_command(label="New tab", accelerator="Ctrl+N",command=new_tab)
filem.add_command(label="New window", accelerator="Ctrl+Shift+N",command=new_window)
filem.add_command(label="Open", accelerator="Ctrl+O",command=open_file)
filem.add_command(label="Save", accelerator="Ctrl+S",command=save)
filem.add_command(label="Save as", accelerator="Ctrl+Shift+S",command=save_as)
filem.add_command(label="Save all", accelerator="Ctrl+Alt+S",command=save_all)
filem.add_separator()
filem.add_command(label="Page setup",command=page_setup)
filem.add_command(label="Print", accelerator="Ctrl+P",command=print)
filem.add_separator()
filem.add_command(label="Close tab", accelerator="Ctrl+W",command=close_tab)
filem.add_command(label="Close window", accelerator="Ctrl+Shift+W",command=close_window)
filem.add_command(label="Exit",command=exit)
menus.add_cascade(label="File",menu=filem)
root.config(menu=menus)
#Edit Menu
def undo():
    pass

def cut():
    text.event_generate(("<>"))

def copy():
    text.event_generate(("<>"))

def paste():
    text.event_generate(("<>"))

def delete():
    pass

def copilot():
    pass

def find():
    pass

def find_next():
    pass

def find_previous():
    pass

def replace():
    pass

def goto():
    pass

def select_all():
    pass

def date_time():
    pass

def font():
    pass

editm=Menu(menus,tearoff=0)
editm.add_command(label="Undo", accelerator="Ctrl+Z",command=undo)
editm.add_separator()
editm.add_command(label="Cut", accelerator="Ctrl+X",command=cut)
editm.add_command(label="Copy", accelerator="Ctrl+C",command=copy)
editm.add_command(label="Paste", accelerator="Ctrl+V",command=paste)
editm.add_command(label="Delete", accelerator="Del",command=delete)
editm.add_separator()
editm.add_command(label="Explain with Copilot", accelerator="Ctrl+E",command=copilot)
editm.add_separator()
editm.add_command(label="Find",accelerator="Ctrl+F",command=find)
editm.add_command(label="Fint next", accelerator="F3",command=find_next)
editm.add_command(label="Find previous", accelerator="Shift+F3",command=find_previous)
editm.add_command(label="Replace", accelerator="Ctrl+H",command=replace)
editm.add_command(label="Goto",accelerator="Ctrl+G",command=goto)
editm.add_separator()
editm.add_command(label="Select all",accelerator="Ctrl+A",command=select_all)
editm.add_command(label="Time/Date",accelerator="F5",command=date_time)
editm.add_separator()
editm.add_command(label="Font",command=font)
menus.add_cascade(label="Edit",menu=editm)
root.config(menu=menus)
#View Menu
def zoom():
    pass

def status_bar():
    pass

def word_wrap():
    pass


viewm=Menu(menus,tearoff=0)
viewm.add_command(label="Zoom",command=zoom)
viewm.add_command(label="Status bar",command=status_bar)
viewm.add_command(label="Word wrap",command=word_wrap)
menus.add_cascade(label="View",menu=viewm)
root.config(menu=menus)

root.mainloop()