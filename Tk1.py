#1.
from tkinter import  *
root=Tk()

root.mainloop()
#2. Implementation of Size of GUI window
from tkinter import *
root = Tk()
root.geometry("400x200")#Width 400 and height 200; format should be ("width x height")
root.mainloop()
#2a. Restrict the size of GUI window using maxsize() and minsize()
from tkinter import *
root =Tk()
root.geometry("400x200")#It's the base size
root.minsize(100,50)#It sets the minimum size of the window; format(width,height)
root.maxsize(800,600)#It sets the maximum size of the window; format(width,height)
root.mainloop()
#3 Implementation of Label
from tkinter import *
root=Tk()
root.geometry("600x500")
root.minsize(300,200)
root.maxsize(800,700)
add_text=Label(text="My Name is Abisekh")
add_text.pack()#Packing The Data to Display it on The Window otherwise it will not be printed on the window
root.mainloop()
#4. Implementation of image in the GUI window
from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.geometry("2560x1440")
image=Image.open(r"C:\Users\abise\OneDrive\Pictures\R.jpg")
photo=ImageTk.PhotoImage(image)
photo_label=Label(image=photo)
photo_label.pack()
root.mainloop()
#4a. Implementation of image in the GUI window
from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.geometry("1200x900")
text=Label(text="Image Gallery")
text.pack()
image1=Image.open(r"C:\Users\abise\OneDrive\Pictures\R.jpg")
photo1=ImageTk.PhotoImage(image1)
photo_label1=Label(image=photo1)
photo_label1.pack()
image2=Image.open(r"C:\Users\abise\OneDrive\Pictures\block diagram.jpg")
photo2=ImageTk.PhotoImage(image2)
photo_label2=Label(image=photo2)
photo_label2.pack()
image3=Image.open(r"C:\Users\abise\OneDrive\Pictures\equivalent_flow_graph.jpg")
photo3=ImageTk.PhotoImage(image3)
photo_label3=Label(image=photo3)
photo_label3.pack()
root.mainloop()
#5. Implementation of Label in the GUI window
from tkinter import *
root=Tk()
root.title("It's A GUI Window")
root.mainloop()
#6. Implementauion Of Different Operations of Label
from tkinter import *
root=Tk()
root.geometry("800x400")
root.title("GUI Window")
text=Label(text='''
        The robot's hardware architecture involves the integration of sensors, actuators, 
        \nand a custom microcontroller circuit. In lieu of Arduino, 
        \na different microcontroller is employed to control the robot's movements and decision-making processes. 
        \nThe chosen microcontroller is selected based on its computational capabilities, input/output options, and power efficiency.
        \nSensors, such as ultrasonic or infrared distance sensors, are strategically placed on the robot to detect obstacles in its path. 
        \nThese sensors provide real-time data to the microcontroller, enabling the robot to make decisions about its movements. 
        \nThe decision-making algorithm is designed to analyse sensor data and determine the appropriate actions for obstacle avoidance.
        \nActuators, such as motors or servos, are used to drive the wheels or control other locomotion mechanisms. 
        \nThe microcontroller regulates the actuator outputs based on the obstacle detection algorithm, 
        \nensuring that the robot manoeuvres around obstacles effectively.
        ''',bg="light blue",fg="brown",font="arial 10 bold",padx=100,pady=30,borderwidth=10,relief=SUNKEN)
text.pack(side=TOP,anchor="center",fill=X,padx=100,pady=140)
root.mainloop()
#7.
from tkinter import *
root=Tk()
root.geometry("500x400")
root.title("GUI Window")
text=Label(text="READY",fg="white",background="dark blue",font=("Agency FB",12,"bold"))
text.pack(side=BOTTOM,fill=X)
root.mainloop()
#8a.
from tkinter import *
root=Tk()
root.geometry("800x600")
l=Label(text="Abisekh")
l.pack(side=LEFT)
l=Label(text="Abisekh")
l.pack(side=LEFT)

root.mainloop()
#8b.
from tkinter import *
root=Tk()
root.geometry("800x600")
l=Label(text="Abisekh")
l.pack(anchor="w")
l1=Label(text="Abisekh")
l1.pack(anchor="w")
root.mainloop()
#8c.
from tkinter import *
root=Tk()
root.geometry("800x600")
l=Label(text="Abisekh")
l.pack(side=LEFT,anchor="w")
l1=Label(text="Abisekh")
l1.pack(side=LEFT,anchor="w")
root.mainloop()

#9. Implementation of Frame in GUI Window
from tkinter import *
root=Tk()
root.geometry("800x600")
f1=Frame(root,bg="black",borderwidth=2)
f1.pack(side=LEFT)
text=Label(f1,text="Frame",bg="blue",fg="white")
text.pack()
root.mainloop()
#9a.
from tkinter import *
root=Tk()
root.geometry("800x600")
f1=Frame(root,borderwidth=2,bg="dark blue",padx=10,pady=10,relief=SUNKEN)
f1.pack(side=LEFT,fill=Y)
text=Label(f1,text="Side bar",bg="orange",font="arial 12 bold",fg="dark blue",padx=10,pady=10)
text.pack()
f2=Frame(root,borderwidth=2,bg="dark blue",padx=10,pady=10,relief=SUNKEN)
f2.pack(side=TOP,fill=X)
text2=Label(f2,text="Welcome to The GUI Window",bg="orange",font="arial 12 bold",fg="dark blue",padx=10,pady=10)
text2.pack()
root.mainloop()
#10. Implementation of Buttons in Gui
from tkinter import *
root=Tk()
root.geometry("800x600")
f1=Frame(root,borderwidth=2,bg="white",padx=10,pady=10,relief=SUNKEN)
f1.pack(side=TOP,fill=X)
button=Button(f1,text="Click Here",font="arial 12 bold",padx=10,pady=10,bg="blue",fg="white")
button.pack()
root.mainloop()
#10a.
from tkinter import *
def button():
        print("It's A Button")
root=Tk()
root.geometry("800x600")
f1=Frame(root,borderwidth=2,bg="white",padx=10,pady=10,relief=SUNKEN)
f1.pack(side=TOP,fill=X)
button=Button(f1,text="Click Here",font="arial 12 bold",padx=10,pady=10,bg="blue",fg="white",command=button)
button.pack()
root.mainloop()
#10b.
from tkinter import *
def button():
        import random
        x=("It's A Button","My First Button","Button Implementation in GUI","Example of Button")
        y=random.choice(x)
        print(y)
root=Tk()
root.geometry("800x600")
f1=Frame(root,borderwidth=2,bg="white",padx=10,pady=10,relief=SUNKEN)
f1.pack(side=TOP,fill=X)
b1=Button(f1,text="Click Here",font="arial 12 bold",padx=10,pady=10,bg="blue",fg="white",command=button)
b1.pack()
b2=Button(f1,text="Click Here",font="arial 12 bold",padx=10,pady=10,bg="blue",fg="white",command=button)
b2.pack()
b3=Button(f1,text="Click Here",font="arial 12 bold",padx=10,pady=10,bg="blue",fg="white",command=button)
b3.pack()
b4=Button(f1,text="Click Here",font="arial 12 bold",padx=10,pady=10,bg="blue",fg="white",command=button)
b4.pack()
root.mainloop()
#10c.
from tkinter import *
def button():
        import random
        x=("It's A Button","My First Button","Button Implementation in GUI","Example of Button")
        y=random.choice(x)
        print(y)
root=Tk()
root.geometry("800x600")
f1=Frame(root,borderwidth=2,bg="white",padx=10,pady=10,relief=SUNKEN)
f1.pack(side=TOP,fill=X)
fill=Label(f1, text="", bg="white")
fill.pack(side=LEFT, expand=True,fill=X)
b1=Button(f1,text="Click Here",font="arial 12 bold",padx=10,pady=10,bg="blue",fg="white",command=button)
b1.pack(side=LEFT)
b2=Button(f1,text="Click Here",font="arial 12 bold",padx=10,pady=10,bg="blue",fg="white",command=button)
b2.pack(side=LEFT)
b3=Button(f1,text="Click Here",font="arial 12 bold",padx=10,pady=10,bg="blue",fg="white",command=button)
b3.pack(side=LEFT)
b4=Button(f1,text="Click Here",font="arial 12 bold",padx=10,pady=10,bg="blue",fg="white",command=button)
b4.pack(side=LEFT)
fill1=Label(f1, text="", bg="white")
fill1.pack(side=LEFT, expand=True,fill=X)

root.mainloop()
#11. Implementaion of Grid in GUI
from tkinter import *
def validate_input(new_value):
    return len(new_value) <= 4  # Only allow input with 4 or fewer characters

def details():
        print(f"Name is {name_Entry.get()}")
        print(f"Password is {password_Entry.get()}")
root=Tk()
root.geometry("800x600")
name=Label(root,text="Name")
name.grid()
password=Label(root,text=("Password"))
password.grid()
n=StringVar()
p=IntVar()
name_Entry=Entry(root,textvariable=n)
name_Entry.grid(row=0,column=1)
password_Entry=Entry(root,validate="key",validatecommand=(root.register(validate_input),"%P"))
password_Entry.grid(row=1,column=1)
Button(root,text="Submit",command=details).grid()
root.mainloop()
#12. Making an Interfase in GUI using Frame and grid
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
root=Tk()
root.geometry("800x600")

f=Frame(root,bg="lightgrey",borderwidth=4,relief=SUNKEN)
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

Button(f,text="Submit",fg="blue",relief="sunken",font="arial 10").grid(row=5,column=1,pady=10)
root.mainloop()
#13.
from tkinter import *

root = Tk()

# Create an Entry widget with initial text
x=Label(root,text="Password")
x.grid(row=0,column=0)
entry = Entry(root)
entry.grid(row=0,column=1)

root.mainloop()
#14. Password input restriction
from tkinter import *

def validate_input(new_value):
    return len(new_value) <= 4  # Only allow input with 4 or fewer characters

root = Tk()

# Create a Label widget
x = Label(root, text="Password")
x.grid(row=0, column=0)

# Create an Entry widget with validation
entry = Entry(root, validate="key", validatecommand=(root.register(validate_input), "%P"))
entry.grid(row=0, column=1)

root.mainloop()
#15. Implementation of Canvas (Line)
from tkinter import *
root=Tk()
win_width=800
win_height=400
root.geometry(f"{win_width}x{win_height}")
can_widget=Canvas(root,width=win_width,height=win_height)
can_widget.pack()

can_widget.create_line(0,0,800,400,fill="red")
can_widget.create_line(0,400,800,0,fill="purple")
can_widget.create_line(0,200,800,200,fill="dark blue")
can_widget.create_line(400,0,400,400,fill="brown")

can_widget.create_rectangle(200,100,600,300)
can_widget.create_oval(200,100,600,300)
can_widget.create_polygon(350,150,450,150,450,250,350,250)
can_widget.create_oval(350,150,450,250,outline="white",width=2)
can_widget.create_text(400,200,text="Abisekh Dey",fill="light blue")

root.mainloop()
#16a. Implementation of Plain Menu
from tkinter import *
root = Tk()
def file():
        print("It's A Menu!")
root.geometry("800x600")
my_menu=Menu(root)
my_menu.add_command(label="File",command=file)
my_menu.add_command(label="Exit",command=exit)#exit is an Inbuild function
root.config(menu=my_menu)
root.mainloop()
#16b. Implementation of Menu inside of Menu
from tkinter import *
root = Tk()
def functions():
        print("New Project,Save,Save as,Print are the sub-menus comes under File Menu!")
root.geometry("800x600")
my_menu=Menu(root)
sub_menu1=Menu(my_menu,tearoff=0)
sub_menu1.add_command(label="New Project",command=functions)
sub_menu1.add_command(label="Save",command=functions)
sub_menu1.add_separator()
sub_menu1.add_command(label="Save as",command=functions)
sub_menu1.add_command(label="Print",command=functions)
my_menu.add_cascade(label="File",menu=sub_menu1)
root.config(menu=my_menu)

sub_menu2=Menu(my_menu,tearoff=0)
sub_menu2.add_command(label="1",command=functions)
sub_menu2.add_command(label="2",command=functions)
sub_menu2.add_separator()
sub_menu2.add_command(label="3",command=functions)
sub_menu2.add_command(label="4",command=functions)
my_menu.add_cascade(label="Edit",menu=sub_menu2)
root.config(menu=my_menu)

root.mainloop()


#16c. Implementation of Menu inside of Menu and a Message box
from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
def functions():
        print("New Project,Save,Save as,Print are the sub-menus comes under File Menu!")
def get_version():
        version=TkVersion
        tmsg.showinfo(title="Version",message=f"Current version {version}")  
def ratings():
        tmsg.askyesnocancel(title="Rate us",message="Rate us")
root.geometry("800x600")
my_menu=Menu(root)
sub_menu1=Menu(my_menu,tearoff=0)
sub_menu1.add_command(label="New Project",command=functions)
sub_menu1.add_command(label="Save",command=functions)
sub_menu1.add_separator()
sub_menu1.add_command(label="Save as",command=functions)
sub_menu1.add_command(label="Print",command=functions)
my_menu.add_cascade(label="File",menu=sub_menu1)
root.config(menu=my_menu)

sub_menu2=Menu(my_menu,tearoff=0)
sub_menu2.add_command(label="1",command=functions)
sub_menu2.add_command(label="2",command=functions)
sub_menu2.add_separator()
sub_menu2.add_command(label="3",command=functions)
sub_menu2.add_command(label="4",command=functions)
my_menu.add_cascade(label="Edit",menu=sub_menu2)
root.config(menu=my_menu)

sub_menu3=Menu(my_menu,tearoff=0)
sub_menu3.add_command(label="Version",command=get_version)
sub_menu3.add_command(label="Rate us",command=ratings)
sub_menu3.add_separator()
sub_menu3.add_command(label="3",command=functions)
sub_menu3.add_command(label="4",command=functions)
my_menu.add_cascade(label="Help",menu=sub_menu3)
root.config(menu=my_menu)

root.mainloop()
#17. Implementation of Epic Sliders
from tkinter import *
import tkinter.messagebox as tmsg

def add_money():
        print(f"Deposit Successful of Amount {my_slider.get()}")
        tmsg.showinfo(title="Status",message=f"Deposit Successful of Amount {my_slider.get()}")

root = Tk()
root.geometry("800x600")

Label(root,text="Enter Amount to Deposit").pack()
my_slider=Scale(root,from_=0,to=50000,orient=HORIZONTAL,tickinterval=5000,length=1000,state="active",fg="red",resolution=5000)
my_slider.pack()
Button(root,text="Add Deposit",command=add_money).pack()

root.mainloop()
#18a.Radiobutton
from tkinter import *
root=Tk()
def ans():
    print(f"ans is {var.get()}")
Label(root,text="If a = 4, find the area of a square?").grid()
var=StringVar()
var.set(0)
x=["4","2","18","16"]
for i in range(len(x)):
    Radiobutton(root,text=x[i],variable=var,value=x[i]).grid()
Button(text="submit",command=ans).grid()
root.mainloop()
#18b. Radiobutton
from tkinter import *
root=Tk()
def ans():
    print(f"ans is {var.get()}")
Label(root,text="If a = 4, find the area of a square?").grid()
var=StringVar()
var.set(0)
x=[4,2,18,16]
for i in range(len(x)):
    Radiobutton(root,text=x[i],variable=var,value=x[i]).grid()
Button(text="submit",command=ans).grid()
root.mainloop()
#19.Implementation of Text widget 
from tkinter import *
root = Tk()
root.geometry("800x600")
Text(root).pack(fill=BOTH,expand=True)
root.mainloop()
#20a.Implementation of Scrollbar 
#21a. Implimentaion of listbox
from tkinter import *
root = Tk()
def add():
        global i
        Lbx.insert(ACTIVE,f"{i}")
        i+=1
i=0
root.geometry("800x600")
Lbx=Listbox(root)
Lbx.pack()
Lbx.insert(END,"First Element of Listbox")
Button(root,text="add",command=add).pack()
root.mainloop()
#21b. Implimentaion of listbox
from tkinter import *
root = Tk()
root.geometry("800x600")
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)

Lbx=Listbox(root,yscrollcommand=scrollbar.set)
Lbx.pack(fill=BOTH,expand=True)

scrollbar.config(command=Lbx.yview)
for i in range(350):
        Lbx.insert(END,f"Item-{i}")
root.mainloop()
#22.Frame inside Frame
from tkinter import *
root=Tk()
root.geometry("800x400")
f=Frame(root,bg="blue")
f.pack(fill=BOTH,expand=True)
Label(f,text="abisekh").pack()

f2=Frame(f,width=100,height=100,bg="red")
f2.pack(expand=True)
root.mainloop()
#23.Making of a Status Bar
from tkinter import *
root=Tk()
root.geometry("800x600")
Label(root,text="Ready",relief="flat",font="arial 12",anchor="w",bg="sky blue").pack(side=BOTTOM,fill=X)
root.mainloop() 
#24.Making of a Status Bar
from tkinter import *
root=Tk()
root.geometry("800x600")
x="Ready"
Label(root,text=x,relief="flat",font="arial 12",anchor="w",bg="sky blue").pack(side=BOTTOM,fill=X)
root.mainloop() 
#25.Making of a Status Bar
from tkinter import *
root=Tk()
root.geometry("800x600")
text=StringVar()
text.set("Ready")
Label(root,textvariable=text,relief="flat",font="arial 12",anchor="w",bg="sky blue").pack(side=BOTTOM,fill=X)
print(text.get())
root.mainloop() 
#26.Updating the Status Bar
from tkinter import *
root=Tk()
def update():
        text.set("Busy...")
        status.update()
        import time
        time.sleep(2)
        text.set("Your System Ready Now")
root.geometry("800x600")
text=StringVar()
text.set("Ready")
status=Label(root,textvariable=text,relief="flat",font="arial 12",anchor="w",bg="sky blue")
status.pack(side=BOTTOM,fill=X)
Button(root,text="Submit",command=update).pack()
root.mainloop() 
#27.Creating Multiple Roots
from tkinter import *
root=Tk()
def update():
        root.destroy()
        r=Tk()
        r.geometry("500x400")
        Label(r,text="Hello").pack()
        r.mainloop()
root.geometry("800x600")
text=StringVar()
text.set("Ready")
status=Label(root,textvariable=text,relief="flat",font="arial 12",anchor="w",bg="sky blue")
status.pack(side=BOTTOM,fill=X)
Button(root,text="Submit",command=update).pack()
root.mainloop() 
#28. Calculator resource
buttons = [
    [('AC', 'pink',30), ('%', 'pink',30), ('<', 'pink',20), ('/', 'pink',10)],
    [('7', 'orange'), ('8', 'orange'), ('9', 'orange'), ('*', 'pink')],
    [('4', 'orange'), ('5', 'orange'), ('6', 'orange'), ('-', 'pink')],
    [('1', 'orange'), ('2', 'orange'), ('3', 'orange'), ('+', 'pink')],
    [('00', 'orange'), ('0', 'orange'), ('.', 'orange'), ('=', 'pink')]
]

print(buttons[0])
print(len(buttons))
print(buttons[0][0])
x,y,z=buttons[0][0]
print(x)
print(y)
print(z,type(z))
#29. use of .get() .cget()
from tkinter import *

root = Tk()

# Using get() with a variable
var = StringVar()
var.set("Hello")
print(var.get())  # Output: Hello

# Using cget() with a widget
button = Button(root, text="Click me")
print(button.cget("text"))  # Output: Click me
l=Label(root,bg="green")
print(l.cget("bg"))

root.mainloop()
#30. Toggle Button
from tkinter import *
root=Tk()
def ch():
    current_col=b.cget("bg") 
    if current_col == "red":
        change_col="green"
        b.config(bg=change_col)
    else:
        change_col="red"
        b.config(bg=change_col)
b=Button(root,text="change",bg="red")
b.config(command=ch)
b.pack()
root.mainloop()
#31. Checkbutton
from tkinter import *
root=Tk()
def ch():
        print(x.get())
x=BooleanVar()
c=Checkbutton(root,text="get",variable=x)
c.pack()
b=Button(root,text="change",bg="red")
b.config(command=ch)
b.pack()
root.mainloop()
#32.
import tkinter as tk

root = tk.Tk()

# Create an Entry widget
# entry = tk.Entry(root,insertbackground="red")
entry=tk.Label(root,text="get")
entry.pack()
print(entry["text"])

root.mainloop()
#33.
import tkinter as tk

root = tk.Tk()

# Create an Entry widget
entry = tk.Entry(root,insertbackground="red")
entry.pack()

root.mainloop()

#34. Digital clock
import tkinter as tk
from datetime import datetime

def update_clock():
    current_time = datetime.now().strftime("Date: %Y-%m-%d & Time: %H:%M:%S")
    label.config(text=current_time)
    label.after(1000, update_clock)  # Update every 1000 milliseconds (1 second)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Create a label to display the time
label = tk.Label(root, font=("arial", 48), fg="blue",bg="yellow")
label.pack(padx=50, pady=20)

# Start the clock update process
update_clock()

# Start the Tkinter event loop
root.mainloop()



from datetime import datetime
import time

def update_clock():
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        print("\r"+current_time, end="", flush=True)
        time.sleep(1)  # Sleep for 1 second before updating the time

# Start updating the clock
update_clock()

from datetime import datetime
import time

def update_clock():
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        print("\r",current_time, end="", flush=True)
        time.sleep(1)  # Sleep for 1 second before updating the time

# Start updating the clock
update_clock()




print("white\rblack")


from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()

def show_message_box():
    v=tmsg.showinfo("Status", "Hello")

# Schedule the display of the message box after 5 seconds
root.after(5000, show_message_box)

root.mainloop()

from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()

def show_message_box():
    global message_window
    message_window = Toplevel(root)
    message_window.title("Status")
    Label(message_window, text="Hello").pack()
    root.after(5000, hide_message_box)

def hide_message_box():
    message_window.destroy()

# Display the custom message box and schedule hiding it after 5 seconds
show_message_box()

root.mainloop()






import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Background Image Example")

# Load the image
image = Image.open("a.jpg")
photo = ImageTk.PhotoImage(image)


# Create a label with the image and add it to the frame
background_label = tk.Label(root, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a frame to hold widgets
frame = tk.Frame(root, width=600, height=400,bg="light blue")

# # Place the frame in the center of the window
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

label = tk.Label(frame, text="Enter Name", font="arial 28 bold", bg="light blue",padx=20)
label.pack(pady=30,fill=tk.X)

v = tk.StringVar()
entry = tk.Entry(frame, textvariable=v, bg="light blue", borderwidth=4, width=20, font="arial 40 bold",relief="solid")
entry.pack(pady=30)


# Add other widgets to the frame if needed
# For example:
# label = tk.Label(frame, text="Hello, World!")
# label.pack()

# Run the GUI
root.mainloop()



from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("400x300")

# Load the image
image = Image.open("3.jpg")
photo = ImageTk.PhotoImage(image)

# Create a canvas
canvas = Canvas(root, width=1280, height=800)
canvas.pack()

# Add the background image to the canvas
canvas.create_image(0, 0, anchor=NW, image=photo)

# Create a frame on top of the canvas
frame = Frame(canvas, bg="light blue", width=300, height=200)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# Add widgets to the frame
label = Label(frame, text="Enter Name", font="arial 28 bold", bg="light blue",padx=20)
label.pack(pady=30,fill=X)

v = StringVar()
entry = Entry(frame, textvariable=v, bg="light blue", borderwidth=4, width=20, font="arial 40 bold",relief="solid")
entry.pack(pady=30)

root.mainloop()
#
import tkinter as tk

class CounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Counter App")

        # Create a Spinbox to serve as the counter
        self.spinbox = tk.Spinbox(root, from_=0, to=100, font=('Helvetica', 24), width=5)
        self.spinbox.pack(pady=20)

        # Initialize the Spinbox value
        self.spinbox.delete(0, tk.END)
        self.spinbox.insert(0, 0)

        # Buttons to manually increase and decrease the counter
        self.increase_button = tk.Button(root, text="Increase", command=self.increase_counter)
        self.increase_button.pack(side=tk.LEFT, padx=20)

        self.decrease_button = tk.Button(root, text="Decrease", command=self.decrease_counter)
        self.decrease_button.pack(side=tk.RIGHT, padx=20)

    def increase_counter(self):
        current_value = int(self.spinbox.get())
        self.spinbox.delete(0, tk.END)
        self.spinbox.insert(0, current_value + 1)

    def decrease_counter(self):
        current_value = int(self.spinbox.get())
        self.spinbox.delete(0, tk.END)
        self.spinbox.insert(0, current_value - 1)

# Create the main application window
root = tk.Tk()
app = CounterApp(root)
root.mainloop()
#Implementation of spin box
from tkinter import *
root=Tk()
spinbox=Spinbox(root, from_=0, to=100, font=('Helvetica', 24), width=5)
spinbox.pack(pady=20)
print(spinbox.get())
root.mainloop()
#
from tkinter import *
root= Tk()
x=10
def get_val():
        global x
        print(x)
Button(root,text="Submit",command=get_val).pack()
root.mainloop()
#
import tkinter as tk

# Create the main window
root = tk.Tk()

# Create a frame
frame = tk.Frame(root)
frame.pack()

# Add some labels to the frame
label1 = tk.Label(frame, text="Label 1")
label1.pack()
label2 = tk.Label(frame, text="Label 2")
label2.pack()
label3 = tk.Label(frame, text="Label 3")
label3.pack()

# Add a button to print all labels
def print_labels():
        # print(frame.winfo_children())
    print(frame.children.values())
    for widget in frame.children.values():
        print(widget)
        # if isinstance(widget, tk.Label):
        #     print(widget.cget("text"))

button = tk.Button(root, text="Print Labels", command=print_labels)
button.pack()

# Start the main loop
root.mainloop()
#
import tkinter as tk

root1 = tk.Tk()

# Create the main frame
f1 = tk.Frame(root1, bg="lavender")
f1.pack(fill=tk.BOTH, expand=True)

# Create a Canvas widget
canvas = tk.Canvas(f1, bg="lavender")
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Add scrollbars to the canvas
x_scrollbar = tk.Scrollbar(f1, orient=tk.HORIZONTAL, command=canvas.xview)
x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
y_scrollbar = tk.Scrollbar(f1, orient=tk.VERTICAL, command=canvas.yview)
y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure the canvas to use the scrollbars
canvas.configure(xscrollcommand=x_scrollbar.set, yscrollcommand=y_scrollbar.set)

# Create a frame inside the canvas to hold widgets
inner_frame = tk.Frame(canvas, bg="lavender")

# Add the inner frame to the canvas
canvas.create_window((0, 0), window=inner_frame, anchor='nw')

# Update the scrollregion of the canvas to match the size of the inner frame
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

inner_frame.bind("<Configure>", on_frame_configure)

# Example widgets in the inner frame
for i in range(50):
    tk.Label(inner_frame, text="Label " + str(i)).grid(row=i, column=0)
    tk.Entry(inner_frame).grid(row=i, column=1)

root1.mainloop()
