import tkinter as tk

root = tk.Tk()  
canvas = tk.Canvas (root, width=200, height=200, bg="white") 
canvas.pack() 
 
 # Прямо задаємо три точки (x1, y1, x2, y2, x3, y3)  
canvas.create_polygon(55, 10, 100, 10, 123, 83, 43, 83, fill='lightgreen', outline='green')
canvas.create_polygon(50, 150, 110, 150, 110, 190, 50, 190, fill='orange', outline='orange')
root.mainloop()
    