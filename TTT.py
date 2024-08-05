#Tic-Tac-Toe Game
from tkinter import*
import tkinter.messagebox as tmsg
root=Tk()

root.geometry("800x800")
root.maxsize(800,800)
root.minsize(800,800)
turn=True
count=0
result=False
val=None
win_patterns=[
    [0,1,2],[3,4,5],
    [6,7,8],[0,3,6],
    [1,4,7],[2,5,8],
    [0,4,8],[2,4,6]
]
buttons=[]

def get_winner():
    global buttons
    global win_patterns
    global result
    global val
    for i in win_patterns:
        print(i[0],i[1],i[2])
        if buttons[i[0]].cget("text")!="" and buttons[i[1]].cget("text")!="" and buttons[i[2]].cget("text")!="":
            if buttons[i[0]].cget("text") == buttons[i[1]].cget("text") and buttons[i[1]].cget("text") == buttons[i[2]].cget("text"):
                if buttons[i[0]].cget("text")=="X" and buttons[i[1]].cget("text")=="X" and buttons[i[2]].cget("text")=="X":
                    for j in range(len(i)):
                        buttons[i[j]].config(bg="light green")
                    result=True
                    val="X"
                    break
                else:
                    for j in range(len(i)):
                        buttons[i[j]].config(bg="light green")
                    result=True
                    val="O"
                    break
    if result==True and val!=None:
        txt=f"Congratulations! Winner is '{val}'"
        l1.config(text=txt,bg="yellow",fg="blue",padx=100)
    if result==False and count==9:
        txt=f"Sorry! Match Draw'"
        l1.config(text=txt,bg="yellow",fg="blue",padx=100)

def operation(btn):
    global turn
    global count
    if turn==True:
        btn.config(text="O",fg="blue")
        turn=False
    else:
        btn.config(text="X",fg="red")
        turn=True
    btn.config(state="disabled",disabledforeground=btn.cget("fg"))# Set disabledforeground to current fg color
    count+=1
    get_winner()
def rstb():
    tmsg.showinfo("status","Starting New Game")
    global turn
    global count
    global result
    for i in buttons:
        i.config(bg="orange",text="",state="normal")
    l1.config(text="",font="arial 30 bold",bg="black",fg="black",width=50)
    turn=True
    count=0
    result=False
f1=Frame(root,bg="black",relief="solid",borderwidth=4)
f1.pack(expand=True,padx=20)
Label(f1,text="Tic-Tac-Toe",font="arial 30 bold",bg="yellow",fg="blue",padx=20).pack(padx=50)
f2=Frame(f1,bg="black",pady=10)
f2.pack()
for i in range(3):
    for j in range(3):
        b=Button(f2,background="orange",text="",font="arial 30 bold",width=5,height=2)
        b.grid(row=i,column=j,padx=5,pady=5)
        b.config(command=lambda button=b: operation(button))  # Pass the button as an argument
        buttons.append(b)
Button(f1,text="Reset Button",bg="light green",font="arial 20 bold",relief="sunken",command=rstb).pack(pady=10)
l1=Label(f1,text="",font="arial 30 bold",bg="black",fg="black",width=50)
l1.pack(padx=20,pady=10)
root.mainloop()