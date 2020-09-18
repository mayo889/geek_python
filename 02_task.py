from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def cons(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def __str__(self):
        return f"Бренд Пальто: {self.name}. Размер: {self.size}"

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size > 70:
            self.__size = 70
        elif size < 30:
            self.__size = 30
        else:
            self.__size = size

    @property
    def cons(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suit(Clothes):
    def __init__(self, name, growth):
        super().__init__(name)
        self.growth = growth

    def __str__(self):
        return f"Бренд Костюма: {self.name}. Рост: {self.growth}"

    @property
    def growth(self):
        return self.__growth

    @growth.setter
    def growth(self, growth):
        if growth > 250:
            self.__growth = 250
        elif growth < 140:
            self.__growth = 140
        else:
            self.__growth = growth

    @property
    def cons(self):
        return round(self.growth * 2 + 0.3, 2)


coat = Coat('Gucci', 90)
suit = Suit('Armani', 260)

print(coat)
print(f"Расход ткани: {coat.cons}")
print('*' * 35)
print(suit)
print(f"Расход ткани: {suit.cons}")
print('*' * 35)
print(f"Общий расход ткани: {coat.cons + suit.cons}")
