import tkinter
from itertools import cycle

colors = cycle(['red', 'yellow', 'green', 'yellow'])


class TrafficLight:
    __color = None

    def __yellow_on(self):
        canvas.itemconfig(oval_red, fill='white')
        canvas.itemconfig(oval_green, fill='white')
        canvas.itemconfig(oval_yellow, fill='white')
        canvas.itemconfig(oval_yellow, fill='yellow')

    def running(self):
        time = 3000
        self.__color = next(colors)
        canvas.itemconfig(oval_red, fill='red')
        for i in range(1000):
            self.__color = next(colors)
            if self.__color == 'red':
                canvas.after(time, lambda: canvas.itemconfig(oval_red, fill='red'))
                time += 3000
            elif self.__color == 'yellow':
                for j in range(3):
                    canvas.after(time, self.__yellow_on)
                    time += 500
                    canvas.after(time, lambda: canvas.itemconfig(oval_yellow, fill='white'))
                    if j != 2:
                        time += 500
            else:
                canvas.after(time, lambda: canvas.itemconfig(oval_green, fill='green'))
                time += 3000


root = tkinter.Tk()
light = TrafficLight()

canvas = tkinter.Canvas(root, width=600, height=600, bg='white')
canvas.pack()

canvas.create_rectangle(50, 50, 250, 430, fill='white', outline='black')
canvas.create_rectangle(140, 430, 160, 600, fill='black')
oval_red = canvas.create_oval(100, 70, 200, 170, fill='white', outline='black')
oval_yellow = canvas.create_oval(100, 190, 200, 290, fill='white', outline='black')
oval_green = canvas.create_oval(100, 310, 200, 410, fill='white', outline='black')

tkinter.Button(root, text="Включить светофор", command=light.running).pack()

root.mainloop()
