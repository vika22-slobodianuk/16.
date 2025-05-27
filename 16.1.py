from tkinter import*
import winsound
from PIL import Image, ImageTk

def play():
    if var.get() == 0:
        winsound.PlaySound("drink_converted.wav", winsound.SND_FILENAME)
    elif var.get() == 1:
        winsound.PlaySound("tea_converted.wav", winsound.SND_FILENAME)
    elif var.get() == 2:
        winsound.PlaySound("water_converted.wav", winsound.SND_FILENAME)
    elif var.get() == 3:
        winsound.PlaySound("coffee_converted.wav", winsound.SND_FILENAME)

root = Tk()
root.minsize(width=300, height=600)
root.title("Словник")
root['bg'] = 'lavender'

frame = LabelFrame(root, text="Виберіть слово", padx=5, bg="lavender", bd=3)
frame.pack()
var = IntVar()
var.set(0)

Radiobutton(frame, bg="lavender", text="Напій", variable=var, value=0).pack(anchor="w")
Radiobutton(frame, bg="lavender", text="Чай", variable=var, value=1).pack(anchor="w")
Radiobutton(frame, bg="lavender", text="Вода", variable=var, value=2).pack(anchor="w")
Radiobutton(frame, bg="lavender", text="Кава", variable=var, value=3).pack(anchor="w")

Button(text="Відтворити", width=15, height=2, bg="lightskyblue", command=play).pack()

canvas = Canvas(root, width=545, height=273, bg='lavender')
canvas.pack()
img = Image.open('drinks.png')
img = img.resize((550, 275))
img = ImageTk.PhotoImage(img)
canvas.create_image(0, 0, image=img, anchor=NW)
canvas.image = img

root.mainloop()
