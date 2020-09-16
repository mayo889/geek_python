from random import choice, randint
import re
import turtle
import tkinter as tk

direction = {'направо': 0, 'вверх': -90, 'вниз': 90, 'влево': 180}


class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False
        self.x = randint(-100, 100)
        self.y = randint(-100, 100)
        self.angle = 0
        self.speed_turtle = int(speed / 300 * 10)

    def get_info(self):
        x = re.findall(r'\w+', str(type(self)))[-1]
        return (f"Машина: {self.name}. Цвет: {self.color}. Скорость: {self.speed}. Является полицией: "
                f"{'да' if self.is_police else 'нет'}. Тип машины: {x}.")

    def go(self):
        t.speed(10)
        t.color(self.color)
        t.up()
        t.goto(self.x, self.y)
        t.down()
        t.right(t.heading() + self.angle)
        t.speed(self.speed_turtle)
        t.forward(50)
        self.x = t.xcor()
        self.y = t.ycor()
        tk.Label(frame_move, text=f"Машина {self.name} начала движение", bg='ghost white').pack()

    def stop(self):
        tk.Label(frame_move, text=f"Машина {self.name} остановилась", bg='ghost white').pack()

    def turn(self):
        name_direction = choice(list(direction.keys()))
        self.angle = direction[name_direction]
        tk.Label(frame_move, text=f"{self.name} собирается поехать {name_direction}", bg='ghost white').pack()

    def show_speed(self):
        tk.Label(frame_move, text=f"Cкорость {self.name}: {self.speed}", bg='ghost white').pack()


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            tk.Label(frame_move, text=f"{self.name} едет с превышением скорости на {self.speed - 60}",
                     bg='ghost white').pack()
        else:
            tk.Label(frame_move, text=f"Cкорость {self.name}: {self.speed}", bg='ghost white').pack()


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            tk.Label(frame_move, text=f"{self.name} едет с превышением скорости на {self.speed - 40}",
                     bg='ghost white').pack()
        else:
            tk.Label(frame_move, text=f"Cкорость {self.name}: {self.speed}", bg='ghost white').pack()


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


def clear_frame():
    global frame_move
    frame_move.destroy()
    frame_move = tk.LabelFrame(root, text="Информация о движении машин", bg='ghost white')
    frame_move.place(x=610, y=210, width=570, height=353)
    tk.Button(root, text="Clear", command=clear_frame).place(x=900, y=573)


town_car = TownCar(70, 'blue', 'lada')
sport_car = SportCar(210, 'green', 'mazda')
work_car = WorkCar(50, 'yellow', 'belaz')
police_car = PoliceCar(110, 'red', 'ford')

# Интерфейс
root = tk.Tk()
root.geometry('1190x610')
canvas = tk.Canvas(root)
canvas.place(x=0, y=0, width=600, height=600)
screen = turtle.TurtleScreen(canvas)
t = turtle.RawTurtle(screen)

# Информация обо всех машинах
frame_info = tk.LabelFrame(root, text="Информация о машинах", bg='ghost white')
frame_info.place(x=610, y=0, width=570, height=100)
tk.Label(frame_info, text=town_car.get_info(), bg='ghost white').pack()
tk.Label(frame_info, text=sport_car.get_info(), bg='ghost white').pack()
tk.Label(frame_info, text=work_car.get_info(), bg='ghost white').pack()
tk.Label(frame_info, text=police_car.get_info(), bg='ghost white').pack()

# Управление TownCar
frame_buttons_1 = tk.LabelFrame(root, text="Управление TownCar", bg='ghost white')
frame_buttons_1.place(x=610, y=110, width=135, height=90)
tk.Button(frame_buttons_1, text="Go", command=town_car.go).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame_buttons_1, text="Stop", command=town_car.stop).grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame_buttons_1, text="Turn", command=town_car.turn).grid(row=0, column=2, padx=5, pady=5)
tk.Button(frame_buttons_1, text="Show speed", command=town_car.show_speed).grid(row=1, column=0,
                                                                                columnspan=3, padx=5, pady=5)

# Управление TownCar
frame_buttons_2 = tk.LabelFrame(root, text="Управление SportCar", bg='ghost white')
frame_buttons_2.place(x=755, y=110, width=135, height=90)
tk.Button(frame_buttons_2, text="Go", command=sport_car.go).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame_buttons_2, text="Stop", command=sport_car.stop).grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame_buttons_2, text="Turn", command=sport_car.turn).grid(row=0, column=2, padx=5, pady=5)
tk.Button(frame_buttons_2, text="Show speed", command=sport_car.show_speed).grid(row=1, column=0,
                                                                                 columnspan=3, padx=5, pady=5)

# Управление WorkCar
frame_buttons_3 = tk.LabelFrame(root, text="Управление WorkCar", bg='ghost white')
frame_buttons_3.place(x=900, y=110, width=135, height=90)
tk.Button(frame_buttons_3, text="Go", command=work_car.go).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame_buttons_3, text="Stop", command=work_car.stop).grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame_buttons_3, text="Turn", command=work_car.turn).grid(row=0, column=2, padx=5, pady=5)
tk.Button(frame_buttons_3, text="Show speed", command=work_car.show_speed).grid(row=1, column=0,
                                                                                columnspan=3, padx=5, pady=5)

# Управление WorkCar
frame_buttons_4 = tk.LabelFrame(root, text="Управление PoliceCar", bg='ghost white')
frame_buttons_4.place(x=1045, y=110, width=135, height=90)
tk.Button(frame_buttons_4, text="Go", command=police_car.go).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame_buttons_4, text="Stop", command=police_car.stop).grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame_buttons_4, text="Turn", command=police_car.turn).grid(row=0, column=2, padx=5, pady=5)
tk.Button(frame_buttons_4, text="Show speed", command=police_car.show_speed).grid(row=1, column=0,
                                                                                  columnspan=3, padx=5, pady=5)

# Вывод информации о движении машин
frame_move = tk.LabelFrame(root, text="Информация о движении машин", bg='ghost white')
frame_move.place(x=610, y=210, width=570, height=353)
tk.Button(root, text="Clear", command=clear_frame).place(x=900, y=573)

root.mainloop()
