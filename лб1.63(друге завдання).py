from tkinter import *

root = Tk()
root.title("Лісовий пейзаж") # Назва вікна

canvas_width = 800
canvas_height = 600
canvas = Canvas(root, width=canvas_width, height=canvas_height, bg="lightskyblue") # Світло-блакитне небо
canvas.pack()

# Елементи лісового пейзажу

# Гори (далекий план)
# Перша гора
canvas.create_polygon(
    0, 400,
    200, 200,
    400, 400,
    fill="darkgray", outline="gray"
)
# Друга гора
canvas.create_polygon(
    300, 450,
    550, 150,
    800, 450,
    fill="gray", outline="darkgray"
)

# Земля / Лісова підстилка
ground_y = canvas_height - 100 # Рівень землі
canvas.create_rectangle(0, ground_y, canvas_width, canvas_height, fill="forestgreen", outline="darkgreen")

# Річка
river_start_x = 0
river_start_y = ground_y - 50
river_end_x = canvas_width
river_end_y = ground_y + 50
canvas.create_polygon(
    river_start_x, river_start_y,
    river_start_x + 150, river_start_y + 20,
    river_end_x - 150, river_end_y - 20,
    river_end_x, river_end_y,
    fill="royalblue", outline="blue"
)

# Дерева (різних розмірів)
def create_tree(x, y, trunk_height, leaves_radius, trunk_color="sienna", leaves_color="limegreen"):
    # Стовбур
    canvas.create_rectangle(x - 15, y - trunk_height, x + 15, y, fill=trunk_color, outline="brown")
    # Листя
    canvas.create_oval(x - leaves_radius, y - trunk_height - leaves_radius,
                       x + leaves_radius, y - trunk_height + leaves_radius,
                       fill=leaves_color, outline="darkgreen")

# Розміщення дерев
create_tree(100, ground_y, 120, 60) # Велике дерево зліва
create_tree(250, ground_y, 100, 50, leaves_color="darkgreen") # Менше дерево
create_tree(400, ground_y, 140, 70) # Найбільше дерево
create_tree(600, ground_y, 90, 45, trunk_color="brown", leaves_color="forestgreen") # Ще одне дерево

# Сонце (або місяць, якщо це сутінки)
sun_center_x = 700
sun_center_y = 80
sun_radius = 40
canvas.create_oval(sun_center_x - sun_radius, sun_center_y - sun_radius,
                   sun_center_x + sun_radius, sun_center_y + sun_radius,
                   fill="yellow", outline="orange")

# Хмари
canvas.create_oval(150, 50, 250, 100, fill="white", outline="lightgray")
canvas.create_oval(180, 70, 280, 120, fill="white", outline="lightgray")
canvas.create_oval(400, 30, 500, 80, fill="white", outline="lightgray")


root.mainloop()