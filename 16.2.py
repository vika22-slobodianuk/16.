from tkinter import * 
import time 
root = Tk() 
root.title("Анімація") 
canvas = Canvas (root, height=300,width=1500,bg='white') 
canvas.pack() 
img = PhotoImage(file='car.png') 
move1=canvas.create_image(10,10,image=img,anchor=NW) 
canvas.image = img 
for i in range(1,100):
    canvas.move (move1,10,0)
    root.update()
    time.sleep(0.01) 
root.mainloop()