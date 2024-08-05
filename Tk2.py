#28a. Implementing GUI in OOPs 
from tkinter import *
class Oops(Tk):
        def __init__(self):
            super().__init__()
        def geo(self):
            self.geometry("800x600")
x=Oops()
x.geo()
x.mainloop()
#28b. Implementing GUI in OOPs 
from tkinter import *
class Oops(Tk):
        def __init__(self):
            super().__init__()
            self.geometry("800x600")
x=Oops()
x.mainloop()
#28a. Implementing GUI in OOPs 
from tkinter import *
class Oops(Tk):
        def __init__(self):
            super().__init__()
x=Oops()
x.geometry("800x600")
x.mainloop()
#29.Create Button and status bar
from tkinter import *
import tkinter.messagebox as tmsg
class Oops(Tk):
        def __init__(self):
            super().__init__()
            self.geometry("800x600")
            self.text=StringVar()
            self.text.set("Ready")
            Label(textvariable=self.text,font="arial 12",bg="sky blue",anchor="w").pack(side=BOTTOM,fill=X)
        def msg(self):
            tmsg.showinfo(title="Status",message="Button Created Successfully")
        def createbutton(self,a):
            Button(text=a,command=self.msg).pack()
            
x=Oops()
x.createbutton("Click Me")
x.mainloop()
#30.Changing Icon
from tkinter import *
root = Tk()
root.geometry("800x600")
root.title("Calculator")
f=Frame(root,bg="white")
f.pack(expand=True)
Label(f,text="Abisekh").pack()
root.wm_iconbitmap("Calculator.ico")
root.configure(bg="dark blue")
root.mainloop()
#31.Finding of Realsize of the window
from tkinter import *
root = Tk()

width=root.winfo_screenwidth()
height=root.winfo_screenheight()

print(f"Dimensions of The Screen is Width({width})xHeight({height})")

root.mainloop()
#32. Destroy a Root
from tkinter import *
root=Tk()
root.geometry("800x600")
Button(root,text="Exit",command=root.destroy).pack()
root.mainloop()



from tkinter import *
root=Tk()
root.geometry("800x600")
def next():
    root.destroy()
    root1=Tk()
    root1.configure(bg="aqua")
    def prev():
        pass
    root1.geometry("600x400")
    Button(root1,text="Previous Page",bg="red",command=prev).pack()
    root1.mainloop()
Button(root,text="Next Page",bg="red",command=next).pack()
root.mainloop()



from tkinter import *

def next():
    root.withdraw()  # Hide the main window
    root1 = Toplevel(root)  # Create a new window
    root1.configure(bg="aqua")
    def prev():
        root1.destroy()  # Destroy the new window
        root.deiconify()  # Restore the main window
    root1.geometry("600x400")
    Button(root1, text="Previous Page", bg="red", command=prev).pack()

root = Tk()
root.geometry("800x600")
Button(root, text="Next Page", bg="red", command=next).pack()
root.mainloop()


from tkinter import *
root = Tk()
root.geometry("800x600")
x=Button(root, text="Next Page", bg="red").pack()
print(x)
root.mainloop()



import tkinter as tk

class PasswordEntry(tk.Entry):
    def __init__(self, master=None, **kwargs):
        tk.Entry.__init__(self, master, **kwargs)
        self.bind('<Key>', self.on_key_press)

    def on_key_press(self, event):
        char = event.char
        if char.isdigit():
            self.insert(tk.END, '*')
        elif event.keysym == 'BackSpace':
            current_position = self.index(tk.INSERT)
            if current_position > 0:
                self.delete(current_position - 1)
        else:
            # Prevent any other characters from being entered
            self.bell()  # Beep to indicate an invalid input

# Create the main window
root = tk.Tk()
root.title("PIN Entry")

# Create the PasswordEntry widget
entry = PasswordEntry(root)
entry.pack(pady=10)

root.mainloop()




from tkinter import *
root = Tk()
def get():
    print(x.get())
    
def validate_input(new_value):
    return len(new_value) <= 4
root.geometry("800x600")
v=StringVar()
x=Entry(root,textvariable=v,font="arial 30 bold",show="*", validate="key", validatecommand=(root.register(validate_input), "%P"))
x.pack()
Button(root,text="Submit",bg="red",command=get).pack()
root.mainloop()


import tkinter as tk

class CountdownTimer:
    def __init__(self, master,time,timer_label):
        self.master = master
        self.master.title("Countdown Timer")
        self.time_remaining = time  # 5 minutes in seconds
        self.timer_label =timer_label
        
    def get_timer(self):
        self.update_timer()

    def update_timer(self):
        minutes = self.time_remaining // 60
        seconds = self.time_remaining % 60
        timer_text = f"{minutes:02}:{seconds:02}"
        self.timer_label.config(text=timer_text)

        if self.time_remaining > 0:
            self.time_remaining -= 1
            self.master.after(1000, self.update_timer)  # Update timer after 1 second
        else:
            self.timer_label.config(text="Time's up!")

root = tk.Tk()
timer_label = tk.Label(root,text="", font=("Arial", 24))
timer_label.pack()
timer = CountdownTimer(root,300,timer_label)
timer.get_timer()
root.mainloop()









from tkinter import *
from datetime import datetime
new_root3=Tk()
new_root3.geometry("1280x800")
new_root3.minsize(1280,800)
new_root3.maxsize(1280,800)
new_root3.configure(bg="lavender")
                                                        
def update_clock():
    current_time = datetime.now().strftime("Date: %Y-%m-%d & Time: %H:%M:%S")
    label.config(text=current_time)
    label.after(1000, update_clock)
                                                        
ff=Frame(new_root3,bg="lavender")
ff.pack(fill=X)
Label(ff,text="Special Operation Panel",bg="red",fg="white",font="arial 28 bold").pack(fill=X)
Label(ff,text="",bg="lavender",font="arial 28 bold").pack(fill=X)
                                                        
ff1=Frame(new_root3,bg="lavender")
ff1.pack(fill=X)
                                            
Button(ff1,text="Get Any Details",bg="light green",font="arial 28 bold",relief="raised",padx=22).grid(row=0,column=0,pady=35)
Label(ff1,text="",bg="lavender",font="arial 28 bold").grid(row=0,column=1,padx=292,pady=35)
Button(ff1,text="Total Deposit",bg="light green",font="arial 28 bold",relief="raised",padx=34).grid(row=0,column=2,pady=35)
Button(ff1,text="ATM Deposit",bg="light green",font="arial 28 bold",relief="raised",padx=45).grid(row=1,column=0,pady=35)
Button(ff1,text="Total Withdraw",bg="light green",font="arial 28 bold",relief="raised",padx=19).grid(row=1,column=2,pady=35)
Button(ff1,text="ATM Balance",bg="light green",font="arial 28 bold",relief="raised",padx=41).grid(row=2,column=0,pady=35)
Button(ff1,text="Exit",bg="light green",font="arial 28 bold",relief="raised",padx=119).grid(row=2,column=2,pady=35)
Button(ff1,text="Today Deposit",bg="light green",font="arial 28 bold",relief="raised",padx=30).grid(row=3,column=0,pady=37)
Button(ff1,text="Today Withdraw",bg="light green",font="arial 28 bold",relief="raised",padx=15).grid(row=3,column=2,pady=37)

                                                        
ff2=Frame(new_root3,bg="yellow")
ff2.pack(fill=X)
label=Label(ff2,fg="blue",bg="yellow",font="arial 20 bold")
label.pack(fill=X)
update_clock()
new_root3.mainloop()


result = any(x > 5 for x in range(10))
print(result)   
#any function only returns true or false 
#any(...): The any() function takes an iterable and returns True if at least one element in the iterable is True, otherwise it returns False. In this case, it checks if any of the boolean values generated by the generator expression are True.
#For each value of x in the range from 0 to 9, the generator expression checks if x is greater than 5.
#If any of the numbers in the range from 0 to 9 are greater than 5, the any() function will return True.

my_list = [False, True, False, False]
result = any(my_list)#it will check if there was any True present in the list or not if present it will print True else False otherwise
print(result) 

from PIL import Image
png_image = Image.open("restaurant.png")
png_image.save("restaurant.ico")