from tkinter import *

root=Tk()

def change():
    from datetime import datetime
    DATE=datetime.today().strftime("%Y-%m-%d")
    global small_scrvar
    global screen
    current_col=button.cget("bg")
    current_txt=button.cget("text")
    if current_col=="red" and current_txt=="Turn On":
        screen.config(state="normal")
        change_col="light green"
        change_txt="Turn Off"
        button.config(bg=change_col)
        button.config(text=change_txt)
        status=small_scrvar.get()
        small_scrvar.set(status+f"Status >>[ACTIVE]           Version: 3.0.3         Date:{DATE}")
    else:
        change_col="red"
        change_txt="Turn On"
        button.config(bg=change_col)
        button.config(text=change_txt)
        small_scrvar.set("")
        scrvar.set("")
        screen.config(state="disabled")
        
def operation(value):
    current_txt=button.cget("text")
    if current_txt=="Turn Off":
        current_val=scrvar.get()
        if value=="AC":
            scrvar.set("")
        elif value=="x":
            scrvar.set(current_val+"*")    
        elif value=="=":
            if current_val.endswith("%"):
                current_val=current_val[:-1]
                current_val=int(current_val)
                result=current_val/100
                scrvar.set(str(result))
            elif current_val.endswith("!"):
                current_val=current_val[:-1]
                current_val=int(current_val)
                for i in range(1,current_val):
                    current_val=current_val*i
                    result=current_val
                    scrvar.set(str(result))
            elif "^" in current_val:
                current_val=current_val.replace("^","**")
            elif "(" in current_val:
                position=current_val.find("(")
                operator=["+","-","*","/"]
                if current_val[position-1] not in operator:
                    current_val=current_val.replace("(","*(")
            try:
                result=eval(current_val)
                scrvar.set(str(result))
            except:
                    scrvar.set("Syntax Error")

        elif value=="<":
            scrvar.set(current_val[:-1])
        else:
            scrvar.set(current_val+value)

def key_press(event):
    key=event.char #event.char represents the character corresponding to the key that was pressed.
    if key=="\r": #carriage return
        key="="
        operation(key)
    if key==" ":
        key="AC"
        operation(key)
        
root.geometry("560x700")
root.maxsize(1280,800)
root.minsize(560,700)
root.title("Calculator")
root.wm_iconbitmap(r"C:\Users\abise\OneDrive\Documents\GUI PYTHON\Calculator.ico")
root.configure(bg="sky blue")

f=Frame(root,relief="solid",bg="sky blue")
f.pack()

scrvar=StringVar()
scrvar.set("")
screen=Entry(f,textvariable=scrvar,font="agencyFb 46 bold",relief="sunken",width=16,borderwidth=4,bg="light grey",justify="right",state="disabled")
screen.pack(padx=10,pady=10)

f=Frame(root,relief="solid",bg="sky blue")
f.pack()
small_scrvar=StringVar()
small_scrvar.set("")
esmall_scrvar=Entry(f,textvariable=small_scrvar,font="agencyFb 12 bold",relief="sunken",borderwidth=4,bg="black",width=50,state="disabled")
esmall_scrvar.pack(side="left",padx=10,pady=10)
button=Button(f,bg="red",text="Turn On",font="agencyFb 10 bold",relief="raised",borderwidth=2)
button.pack(side="left",padx=10,pady=10)
button.config(command=change)
    
buttons = [
    [('AC', 'light green',21), ('%', 'pink',34), ('^', 'pink',30), ('<', 'red',35)],
    [('!', 'pink',44), ('(', 'pink',44), (')', 'pink',36), ('/', 'pink',41)],
    [('7', 'orange',40), ('8', 'orange',38), ('9', 'orange',31), ('x', 'pink',37)],
    [('4', 'orange',40), ('5', 'orange',38), ('6', 'orange',31), ('-', 'pink',39)],
    [('1', 'orange',40), ('2', 'orange',38), ('3', 'orange',31), ('+', 'pink',34)],
    [('00', 'orange',27), ('0', 'orange',38), ('.', 'orange',38), ('=', 'light green',33)]
]
for i in range(len(buttons)):
    f=Frame(root,bg="sky blue")
    f.pack()
    for j in range(len(buttons[i])):
        txt,colour,x=buttons[i][j]
        Button(f,text=txt,font="agencyFb 30 bold",relief="raised",padx=x,bg=colour,command=lambda t=txt: operation(t)).pack(side=LEFT,padx=5,pady=5)
        
root.bind("<Key>",key_press) #Event; if a key press event occurs from the key board then it will call the key_press function
        
root.mainloop()