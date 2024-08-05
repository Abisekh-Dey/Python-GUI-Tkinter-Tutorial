from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()

def rate():
    if experience.get()<5:
        rev="Bad"
    elif experience.get()==5:
        rev="Good"
    else:
        rev="Very Good"
    with open("b.txt","a") as f:
        f.write(f"Name: {name.get()}-> Rating: {rev}\n")
    tmsg.showinfo(title="Submit",message="Thank You for Your Valuable Feedback")

root.geometry("1000x800")
f=Frame(root,borderwidth=4,relief=SOLID,bg="light grey")
f.pack(expand=True)

Label(f,text="Rate Your Experience",font="calibri 16 bold",bg="light grey").grid(row=0,column=3)
Label(f,text="Your Name",font="calibri 16 ",bg="light grey",relief=RAISED).grid(row=1,column=0)
Label(f,text="Your Experience in 10",font="calibri 16 ",bg="light grey",relief=RAISED).grid(row=2,column=0)

cname=StringVar()

name=Entry(f,textvariable=cname,width=80)
name.grid(row=1,column=3)

experience=Scale(f,from_=0,to=10,orient=HORIZONTAL,tickinterval=1,length=500,state="active",fg="red",resolution=1,bg="light grey",activebackground="aqua",highlightbackground="grey",)
experience.grid(row=2,column=3,pady=10,padx=10)

Button(f,text="Submit",font="calibri 12 bold",bg="light green",relief=GROOVE,command=rate).grid(row=3,column=3,pady=10,padx=10)

root.mainloop()


