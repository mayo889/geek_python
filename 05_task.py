class Stationery:
    title = None

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def __init__(self):
        self.title = "Ручка"

    def draw(self):
        print(f"Запуск отрисовки предметом {self.title}")


class Pencil(Stationery):
    def __init__(self):
        self.title = "Карандаш"

    def draw(self):
        print(f"Запуск отрисовки предметом {self.title}")


class Handle(Stationery):
    def __init__(self):
        self.title = "Маркер"

    def draw(self):
        print(f"Запуск отрисовки предметом {self.title}")


pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()
