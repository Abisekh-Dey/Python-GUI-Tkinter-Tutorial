from tkinter import *

root = Tk()

def geo():
    root.geometry(f"{win_width.get()}x{win_height.get()}")
    root.maxsize(win_width.get(),win_height.get())
    print("Dimension Changed Successfully!")

win_width=IntVar()
win_height=IntVar()

Label(root,text="Change Dimensions of GUI Window",font="calibri 16 bold").grid(row=0,column=3)
Label(root,text="Enter Width",font="calibri 12").grid(row=1,column=0)
Label(root,text="Enter Height",font="calibri 12").grid(row=2,column=0)

width=Entry(root,textvariable=win_width)
height=Entry(root,textvariable=win_height)

width.grid(row=1,column=3)
height.grid(row=2,column=3)

Button(root,text="Apply",font="calibri 12",bg="aqua",relief=FLAT,command=geo).grid(row=3,column=3,pady=10)
root.mainloop()