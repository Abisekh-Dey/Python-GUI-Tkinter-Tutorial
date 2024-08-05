#1. Using Global variable GUI window Resizer
from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
width=1200
height=600

root.geometry(f"{width}x{height}")
def change_size():
    global width, height
    a=tmsg.askyesno(title="Save Changes",message="Save Changes ?")
    if a==True:
        root.geometry(f"{width1.get()}x{height1.get()}")
        if width1.get()<width or height1.get()<height:
            tmsg.showinfo(title="Status",message=f"GUI Window Size Reduced to {width1.get()}x{height1.get()}")
        elif width1.get()>width or height1.get()>height:
            tmsg.showinfo(title="Status",message=f"GUI Window Size Increased to {width1.get()}x{height1.get()}")
        else:
            tmsg.showinfo(title="Status",message=f"GUI Window Size Unchanged at {width1.get()}x{height1.get()}")
        width=width1.get()
        height=height1.get()
    else:
        tmsg.showinfo(title="Status",message="Size Unchanged")

f=Frame(root,borderwidth=4,relief=SOLID,bg="light grey")
f.pack(expand=TRUE)
Label(f,text="Change Dimensions of GUI Window",font="calibri 16 bold",bg="light grey").grid(row=0,column=3)
Label(f,text="Enter Width",font="calibri 12",bg="light grey",relief=RAISED).grid(row=1,column=0)
Label(f,text="Enter Height",font="calibri 12",bg="light grey",relief=RAISED).grid(row=2,column=0)

width1=Scale(f,from_=0,to=1800,orient=HORIZONTAL,tickinterval=200,length=1000,state="active",fg="red",resolution=200,bg="light grey",activebackground="aqua",highlightbackground="grey")
width1.set(width)
width1.grid(row=1,column=3,padx=10,pady=10)
height1=Scale(f,from_=0,to=1000,orient=HORIZONTAL,tickinterval=100,length=1000,state="active",fg="red",resolution=100,bg="light grey",activebackground="aqua",highlightbackground="grey")
height1.set(height)
height1.grid(row=2,column=3,padx=10,pady=10)

Button(f,text="Save Changes",font="calibri 12 bold",bg="aqua",relief=GROOVE,command=change_size).grid(row=3,column=3,pady=10)
root.mainloop()

#2. Using Lambda and Mutable object(List) GUI window Resizer
from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
width = [1200]
height = [600]

root.geometry(f"{width[0]}x{height[0]}")

def change_size(width, height):
    a = tmsg.askyesno(title="Save Changes", message="Save Changes ?")
    if a:
        root.geometry(f"{width1.get()}x{height1.get()}")
        if width1.get() < width[0] or height1.get() < height[0]:
            tmsg.showinfo(title="Status", message=f"GUI Window Size Reduced to {width1.get()}x{height1.get()}")
        elif width1.get() > width[0] or height1.get() > height[0]:
            tmsg.showinfo(title="Status", message=f"GUI Window Size Increased to {width1.get()}x{height1.get()}")
        else:
            tmsg.showinfo(title="Status", message=f"GUI Window Size Unchanged at {width1.get()}x{height1.get()}")
        
        width[0] = width1.get()
        height[0] = height1.get()
    else:
        tmsg.showinfo(title="Status", message="Size Unchanged")

f = Frame(root, borderwidth=4, relief=SOLID, bg="light grey")
f.pack(expand=TRUE)

Label(f, text="Change Dimensions of GUI Window", font="calibri 16 bold", bg="light grey").grid(row=0, column=3)
Label(f, text="Enter Width", font="calibri 12", bg="light grey").grid(row=1, column=0)
Label(f, text="Enter Height", font="calibri 12", bg="light grey").grid(row=2, column=0)

width1 = Scale(f, from_=0, to=1800, orient=HORIZONTAL, tickinterval=200, length=1000, state="active",
               fg="red", resolution=200, bg="light grey", activebackground="aqua", highlightbackground="grey")
width1.set(width[0])
width1.grid(row=1, column=3)

height1 = Scale(f, from_=0, to=1000, orient=HORIZONTAL, tickinterval=100, length=1000, state="active",
                fg="red", resolution=100, bg="light grey", activebackground="aqua", highlightbackground="grey")
height1.set(height[0])
height1.grid(row=2, column=3)

Button(f, text="Save Changes", font="calibri 12 bold", bg="aqua", relief=GROOVE,
       command=lambda: change_size(width, height)).grid(row=3, column=3, pady=10)

root.mainloop()
