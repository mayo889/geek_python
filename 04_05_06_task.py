from abc import ABC, abstractmethod


class Stock:
    printers = []
    scanners = []
    xeroxes = []

    @classmethod
    def add_equipment(cls):
        ans_name = int(input("Добавить принтер: 1, сканер: 2, ксерокс: 3. Ответ: "))
        name, number, price = input("Введите модель, количество и цену через пробел: ").split()
        if ans_name == 1:
            pos = len(cls.printers)
            cls.printers.append(Printer(name, number, price))
            if cls.printers[pos].number == 0 or cls.printers[pos].price == 0:
                print("\tКоличество и цена должны быть числом и больше нуля!")
                cls.printers.pop(pos)
        elif ans_name == 2:
            pos = len(cls.scanners)
            cls.scanners.append(Scanner(name, number, price))
            if cls.scanners[pos].number == 0 or cls.scanners[pos].price == 0:
                print("\tКоличество и цена должны быть числом и больше нуля!")
                cls.scanners.pop(pos)
        elif ans_name == 3:
            pos = len(cls.xeroxes)
            cls.xeroxes.append(Xerox(name, number, price))
            if cls.xeroxes[pos].number == 0 or cls.xeroxes[pos].price == 0:
                print("\tКоличество и цена должны быть числом и больше нуля!")
                cls.xeroxes.pop(pos)
        else:
            print("\tТакого ответа нет!")

    @staticmethod
    def print_objects(array):
        for elem in array:
            print(f"\t\t{elem}")

    @classmethod
    def get_info(cls):
        print("\tПринтеры на складе:")
        Stock.print_objects(cls.printers)
        print("\tСканеры на складе:")
        Stock.print_objects(cls.scanners)
        print("\tКсероксы на складе:")
        Stock.print_objects(cls.xeroxes)

    @classmethod
    def update_info(cls):
        ans_name = int(input("Обновить данные для принтера: 1, сканера: 2, ксерокса: 3. Ответ: "))
        name = input("Введите модель, для которой обновить информацию: ")
        number, price = input("Введите НОВОЕ значение количества и цены через пробел: ").split()
        if not ((number.isdigit() and int(number) > 0) and (price.isdigit() and int(price) > 0)):
            print("\tДля изменения данных количество и цена должны быть числами и больше нуля!")
        else:
            if ans_name == 1:
                for elem in cls.printers:
                    if elem.name == name:
                        elem.number = number
                        elem.price = price
            elif ans_name == 2:
                for elem in cls.scanners:
                    if elem.name == name:
                        elem.number = number
                        elem.price = price
            elif ans_name == 3:
                for elem in cls.xeroxes:
                    if elem.name == name:
                        elem.number = number
                        elem.price = price
            else:
                print("\tТакого ответа нет!")

    @classmethod
    def del_object(cls):
        ans_name = int(input("Удалить принтер: 1, сканер: 2, ксерокс: 3. Ответ: "))
        name = input("Введите модель оргтехники, которую необходимо удалить: ")
        if ans_name == 1:
            for i in range(len(cls.printers)):
                if cls.printers[i].name == name:
                    cls.printers.pop(i)
        elif ans_name == 2:
            for i in range(len(cls.scanners)):
                if cls.scanners[i].name == name:
                    cls.scanners.pop(i)
        elif ans_name == 3:
            for i in range(len(cls.xeroxes)):
                if cls.xeroxes[i].name == name:
                    cls.xeroxes.pop(i)
        else:
            print("\tТакого ответа нет!")


class Equipment(ABC):
    def __init__(self, name, number, price):
        self.name = name
        self.number = number
        self.price = price

    def __str__(self):
        return f"Фирма: {self.name}. Количество: {self.number}. Цена: {self.price}"

    @staticmethod
    @abstractmethod
    def what_can_do():
        pass

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        self.__number = int(number) if (number.isdigit() and int(number) > 0) else 0

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = int(price) if (price.isdigit() and int(price) > 0) else 0


class Printer(Equipment):
    @staticmethod
    def what_can_do():
        print("\tПринтер - устройство вывода текстовой или графической информации")


class Scanner(Equipment):
    @staticmethod
    def what_can_do():
        print("\tСканер - устройство для преобразования изображения в цифровой формат")


class Xerox(Equipment):
    @staticmethod
    def what_can_do():
        print("\tСканер - устройство для ксерографического копирования")


while True:
    print('-' * 98)
    print("Выход из программы: 0.   Добавить товар на склад: 1.   Получить всю аналитику данных со склада: 2.\n"
          "Узнать возможности оргтехники: 3.   Обновить информацию о товаре: 4.   Удалить товар из склада: 5.")
    ans = int(input("Ответ: "))
    if ans == 0:
        break
    elif ans == 1:
        Stock.add_equipment()
    elif ans == 2:
        Stock.get_info()
    elif ans == 3:
        Printer.what_can_do()
        Scanner.what_can_do()
        Xerox.what_can_do()
    elif ans == 4:
        Stock.update_info()
    elif ans == 5:
        Stock.del_object()
