from tkinter import *
import tkinter.messagebox as tmsg

root=Tk()

def fdetails():
    with open("a.txt","a") as f:
        f.write(f"Name={sname.get()},University Roll No={sroll.get()},Registration No={sreg.get()},Year={syear.get()},Gender={gender.get()},Department={trade.get()},Semester={semester.get()}\n")
    tmsg.showinfo(title="Status",message=f"Name={sname.get()},University Roll No={sroll.get()},Registration No={sreg.get()},Year={syear.get()},Gender={gender.get()},Department={trade.get()},Semester={semester.get()} Saved Successfully!")
root.geometry("800x600")
f=Frame(root,bg="light grey",relief=SOLID)
f.pack(expand=True)
Label(f,text="Student Form",font="comisence 12 bold",bg="light grey",relief="raised").grid(row=0,column=3,pady=10)
details=["Name","University Roll No","Registration No","Year","Gender","Department","Semester"]
for i in range(len(details)):
    Label(f,text=details[i],font="arial 12",bg="light grey",relief="groove",justify="left").grid(row=i+1,column=0,padx=10,pady=5)
    
sname=StringVar()
sroll=StringVar()
sreg=StringVar()
syear=StringVar()
gender=StringVar()
gender.set("gender")
trade=StringVar()
trade.set("trade")
semester=StringVar()
semester.set("semester")
semester=StringVar()
semester.set("semester")

ename=Entry(f,textvariable=sname)
eroll=Entry(f,textvariable=sroll)
ereg=Entry(f,textvariable=sreg)
eyear=Entry(f,textvariable=syear)

ename.grid(row=1,column=3,padx=10,pady=5)
eroll.grid(row=2,column=3,padx=10,pady=5)
ereg.grid(row=3,column=3,padx=10,pady=5)
eyear.grid(row=4,column=3,padx=10,pady=5)

g=["Male","Female","Other"]
for i in range(len(g)):
    Radiobutton(f,text=g[i],variable=gender,value=g[i],bg="light grey",font="arial 12").grid(row=5,column=i+2,padx=10,pady=5)
t=["ECE","CSE","CE","ME","EE"]
for i in range(len(t)):
    Radiobutton(f,text=t[i],variable=trade,value=t[i],bg="light grey",font="arial 12").grid(row=6,column=i+2,padx=10,pady=5)
so=["semester 1","semester 3","semester 5","semester 7"]
for i in range(len(so)):
    Radiobutton(f,text=so[i],variable=semester,value=so[i],bg="light grey",font="arial 12").grid(row=7+i,column=2,padx=10,pady=5)
se=["semester 2","semester 4","semester 6","semester 8"]
for i in range(len(se)):
    Radiobutton(f,text=se[i],variable=semester,value=se[i],bg="light grey",font="arial 12").grid(row=7+i,column=3,padx=10,pady=5)

Button(f,text="Submit",bg="light green",font="arial 12 bold",relief=FLAT,command=fdetails).grid(row=11,column=3,pady=10)
root.mainloop()