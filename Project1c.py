
from tkinter import *
from PIL import  ImageTk, Image

def every_100(text):
    final_text = ""
    for i in range(0, len(text)):
        final_text +=text[i]
        if i%200==0 and i!=0:#i!=0 because if i == 0 then i%200 will also be 0 so it will print newline after the first character to avoid this we have to do i!=0
            final_text += "\n"
    return final_text



root = Tk()
root.title("Deys News")
root.geometry("1000x1000")

texts = []
photos = []
for i in range(0, 3):
    with open(f"{i+1}.txt") as f:
        text = f.read()
        texts.append(every_100(text))

    image = Image.open(f"{i+1}.jpg")
    #TODO: Resize these images
    image = image.resize((140, 215))
    photos.append(ImageTk.PhotoImage(image))

f0 = Frame(root)
Label(f0, text="Deys News", font="lucida 24 bold").pack()
Label(f0, text="March 2, 2024", font="lucida 12 bold").pack()
f0.pack()

for i in range(len(texts)):
    f1 = Frame(root)
    f1.pack(anchor="w",fill=X)
    Label(f1, text=texts[i]).pack(side="left",expand=TRUE)
    Label(f1, image=photos[i]).pack()
    
root.mainloop()