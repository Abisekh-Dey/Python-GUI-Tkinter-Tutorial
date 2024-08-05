from tkinter import *

def getvals():
    print("Form Submitted Successfully!")
    with open("C:\\Users\\abise\\OneDrive\\Documents\\GUI PYTHON\\a.txt","a") as f:
        f.write(f"Customer Name: {cname.get()},Contact Number: {ccont.get()},Gender: {cgender.get()},Emergency Contact Number: {cecontact.get()},Food Service: {foodservice.get()}\n")

root=Tk()
root.geometry("500x300")
root.maxsize(600,400)
root.minsize(500,300)
form=Label(root,text="Welcome To Anywhere Travel Agency",font="comisence 12 bold")
form.grid(row=0,column=3,pady=10)
name=Label(root,text="Name",font="arial 12")
cont=Label(root,text="Contact/Phone No",font="arial 12")
gender=Label(root,text="Gender",font="arial 12")
econtact=Label(root,text="Emergency Contact",font="arial 12")
payment=Label(root,text="Payment Mode",font="arial 12")

name.grid(row=1,column=2,padx=10)
cont.grid(row=2,column=2,padx=10)
gender.grid(row=3,column=2,padx=10)
econtact.grid(row=4,column=2,padx=10)
payment.grid(row=5,column=2,padx=10)

cname=StringVar()
ccont=StringVar()
cgender=StringVar()
cecontact=StringVar()
cpayment=StringVar()
foodservice=IntVar()

ename=Entry(root,textvariable=cname)
econt=Entry(root,textvariable=ccont)
egender=Entry(root,textvariable=cgender)
eecontact=Entry(root,textvariable=cecontact)
epayment=Entry(root,textvariable=cpayment)

ename.grid(row=1,column=3)
econt.grid(row=2,column=3)
egender.grid(row=3,column=3)
eecontact.grid(row=4,column=3)
epayment.grid(row=5,column=3)

fs=Checkbutton(root,text="Want to Pre-book Meals?",font="arial 12",variable=foodservice)
fs.grid(row=6,column=3,pady=10)

b=Button(root,text="Submit to Anywhere Travel Agency",command=getvals,font="arial 12",relief=SOLID,bg="aqua").grid(row=7,column=3)
root.mainloop()