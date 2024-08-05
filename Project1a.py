from tkinter import *
from PIL import Image, ImageTk
root=Tk()
root.title("Newspaper")
root.geometry("800x600")
i1=Image.open("1.jpg")
ri1=i1.resize((140,215))
p1=ImageTk.PhotoImage(ri1)
f1=Frame(root,bg="lightgrey",borderwidth=6,relief=SUNKEN)
f1.pack(side=TOP,fill=X)
text=Label(f1,text="Newspaper",bg="light blue")
text.pack(side=TOP)
s1=Label(f1,image=p1)
s1.pack(side=LEFT)
t1=Label(f1,text='''
        The outcomes of this project include a fully functional obstacle-avoiding robot 
        \nthat demonstrates the feasibility of creating autonomous robotic systems 
        \nwithout relying on popular microcontroller platforms like Arduino. 
        \nThe project's findings contribute to the exploration of alternative 
        \nhardware solutions for robotics enthusiasts and researchers seeking cost-effective and versatile designs. 
         ''',bg="grey",fg="brown",compound='left',font="AgencyFB 12 bold")
t1.pack(expand=TRUE,fill=X)
f2=Frame(root,bg="lightgrey",borderwidth=6,relief=SUNKEN)
f2.pack(side=TOP,fill=X)
i2=Image.open("2.jpg")
ri2=i2.resize((140,215))
p2=ImageTk.PhotoImage(ri2)
s2=Label(f2,image=p2)
s2.pack(side=LEFT)
t2=Label(f2,text='''
        The outcomes of this project include a fully functional obstacle-avoiding robot 
        \nthat demonstrates the feasibility of creating autonomous robotic systems 
        \nwithout relying on popular microcontroller platforms like Arduino. 
        \nThe project's findings contribute to the exploration of alternative 
        \nhardware solutions for robotics enthusiasts and researchers seeking cost-effective and versatile designs. 
         ''',bg="grey",fg="brown",compound='left',font="AgencyFB 12 bold")
t2.pack(expand=TRUE,fill=X)
f3=Frame(root,bg="lightgrey",borderwidth=6,relief=SUNKEN)
f3.pack(side=TOP,fill=X)
i3=Image.open("3.jpg")
ri3=i3.resize((140,215))
p3=ImageTk.PhotoImage(ri3)
s3=Label(f3,image=p3)
s3.pack(side=LEFT)
t3=Label(f3,text='''
        The outcomes of this project include a fully functional obstacle-avoiding robot 
        \nthat demonstrates the feasibility of creating autonomous robotic systems 
        \nwithout relying on popular microcontroller platforms like Arduino. 
        \nThe project's findings contribute to the exploration of alternative 
        \nhardware solutions for robotics enthusiasts and researchers seeking cost-effective and versatile designs. 
         ''',bg="grey",fg="brown",compound='left',font="AgencyFB 12 bold")
t3.pack(expand=TRUE,fill=X)

root.mainloop()