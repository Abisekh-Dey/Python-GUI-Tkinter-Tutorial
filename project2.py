from tkinter import *
from PIL import Image,ImageTk
def validate_input(new_value):
    return len(new_value) <= 4  # Only allow input with 4 or fewer characters
def get_captcha():
        import string
        import random
        str=string.ascii_letters+string.digits
        captcha="".join(random.choice(str) for i in range(6))
        return captcha
def refresh_captcha():
        capt = get_captcha()
        captcha.config(text=capt)
def operation():
        print("Successful!")
root=Tk()
root.geometry("800x600")

f=Frame(root,bg="lightgrey",borderwidth=4,relief=SOLID)
f.pack(expand=True)

name=Label(f,text="Student Name",font="arial 12",fg="black",bg="lightgrey")
name.grid(padx=10,pady=10)

password=Label(f,text="Password",font="arial 12",fg="black",bg="lightgrey")
password.grid(padx=10,pady=10)

name_Entry=Entry(f,textvariable=StringVar())
name_Entry.grid(row=0,column=1,pady=10,padx=10)

password_Entry=Entry(f,textvariable=StringVar(),validate="key",validatecommand=(root.register(validate_input),"%P"))
password_Entry.grid(row=1,column=1,padx=10,pady=10)

cap=Label(f,text="Captcha",font="arial 12",fg="black",bg="lightgrey")
cap.grid(row=3,column=0,pady=10)

captcha=Label(f,text=get_captcha(),bg="light blue",fg="black",font="arial 12 italic")
captcha.grid(row=3,column=1,pady=10)

image=Image.open("refresh.png")
reimage=image.resize((20,20))
refresh_icon=ImageTk.PhotoImage(image=reimage)

captcha_refresh_button = Button(f, image=refresh_icon, relief="flat", command=refresh_captcha,bg="light grey")
captcha_refresh_button.grid(row=3, column=2)

vcap=Label(f,text="Enter Captcha",font="arial 12",fg="black",bg="lightgrey")
vcap.grid(row=4,column=0)

vcap_Entry=Entry(f)
vcap_Entry.grid(row=4,column=1,pady=10)

Button(f,text="LOGIN",fg="white",relief=FLAT,font="arial 10",bg="green",command=operation).grid(row=5,column=1,pady=10)
root.mainloop()
