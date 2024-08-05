from tkinter import *

root=Tk()
def operation(value):
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
        else:
            try:
                result=eval(current_val)
                scrvar.set(str(result))
            except:
                scrvar.set("Syntax Error")

    elif value=="<":
        scrvar.set(current_val[:-1])
    else:
        scrvar.set(current_val+value)
root.geometry("600x630")
root.maxsize(600,630)
root.minsize(600,630)
root.title("Calculator")
root.wm_iconbitmap(r"C:\Users\abise\OneDrive\Documents\GUI PYTHON\Calculator.ico")
root.configure(bg="sky blue")

f=Frame(root,relief="solid",bg="sky blue")
f.pack()

scrvar=StringVar()
scrvar.set("")
screen=Entry(f,textvariable=scrvar,font="agencyFb 48 bold",relief="groove",width=16,justify="right")
screen.pack(padx=10,pady=10)

buttons = [
    [('AC', 'pink',20), ('%', 'pink',30), ('<', 'pink',30), ('/', 'pink',40)],
    [('7', 'orange',40), ('8', 'orange',38), ('9', 'orange',31), ('x', 'pink',37)],
    [('4', 'orange',40), ('5', 'orange',38), ('6', 'orange',31), ('-', 'pink',39)],
    [('1', 'orange',40), ('2', 'orange',38), ('3', 'orange',31), ('+', 'pink',34)],
    [('00', 'orange',27), ('0', 'orange',38), ('.', 'orange',38), ('=', 'pink',33)]
]
for i in range(len(buttons)):
    f=Frame(root,bg="sky blue")
    f.pack()
    for j in range(len(buttons[i])):
        txt,colour,x=buttons[i][j]
        Button(f,text=txt,font="agencyFb 35 bold",relief="raised",padx=x,bg=colour,command=lambda t=txt: operation(t)).pack(side=LEFT,padx=5,pady=5)
        
root.mainloop()