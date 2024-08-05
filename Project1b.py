from tkinter import *
from PIL import Image, ImageTk
root=Tk()
root.title("Newspaper")
root.geometry("800x600")
f=Frame(root,bg="lightgrey",borderwidth=6,relief=SUNKEN)
f.pack(side=TOP,fill=BOTH,expand=TRUE)
i1=Image.open("1.jpg")
ri1=i1.resize((140,225))
p1=ImageTk.PhotoImage(ri1)
text=Label(f,text="Newspaper",bg="light blue")
text.grid(row=0,column=3)
s1=Label(f,image=p1)
s1.grid(row=1,column=0)
t1=Label(f,text='''
        The outcomes of this project include a fully functional obstacle-avoiding robot 
        \nthat demonstrates the feasibility of creating autonomous robotic systems 
        \nwithout relying on popular microcontroller platforms like Arduino. 
        \nThe project's findings contribute to the exploration of alternative 
        \nhardware solutions for robotics enthusiasts and researchers seeking cost-effective and versatile designs. 
         ''',bg="grey",fg="brown",compound='left',font="AgencyFB 12 bold",padx=160,pady=7)
t1.grid(row=1,column=3)
i2=Image.open("2.jpg")
ri2=i2.resize((140,225))
p2=ImageTk.PhotoImage(ri2)
s2=Label(f,image=p2)
s2.grid(row=2,column=0)
t2=Label(f,text='''
        The outcomes of this project include a fully functional obstacle-avoiding robot 
        \nthat demonstrates the feasibility of creating autonomous robotic systems 
        \nwithout relying on popular microcontroller platforms like Arduino. 
        \nThe project's findings contribute to the exploration of alternative 
        \nhardware solutions for robotics enthusiasts and researchers seeking cost-effective and versatile designs. 
         ''',bg="grey",fg="brown",compound='left',font="AgencyFB 12 bold",padx=160,pady=7)
t2.grid(row=2,column=3)
i3=Image.open("3.jpg")
ri3=i3.resize((140,225))
p3=ImageTk.PhotoImage(ri3)
s3=Label(f,image=p3)
s3.grid(row=3,column=0)
t3=Label(f,text='''
        The outcomes of this project include a fully functional obstacle-avoiding robot 
        \nthat demonstrates the feasibility of creating autonomous robotic systems 
        \nwithout relying on popular microcontroller platforms like Arduino. 
        \nThe project's findings contribute to the exploration of alternative 
        \nhardware solutions for robotics enthusiasts and researchers seeking cost-effective and versatile designs. 
         ''',bg="grey",fg="brown",compound='left',font="AgencyFB 12 bold",padx=160,pady=7)
t3.grid(row=3,column=3)

root.mainloop()