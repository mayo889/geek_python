class Cell:
    def __init__(self, size):
        self.size = size

    def __add__(self, other):
        return self.size + other.size

    def __sub__(self, other):
        if self.size > other.size:
            return self.size - other.size
        else:
            return other.size - self.size

    def __mul__(self, other):
        return self.size * other.size

    def __floordiv__(self, other):
        return self.size // other.size

    def make_order(self, x):
        return ''.join(['\n*' if (i % x == 0 and i != 0) else '*' for i in range(len('*' * self.size))])


cell_1 = Cell(3)
cell_2 = Cell(15)

print(f"Результат сложения двух клеток: {cell_1 + cell_2}")
print(f"Результат вычитания двух клеток: {cell_1 - cell_2}")
print(f"Результат умножения двух клеток: {cell_1 * cell_2}")
print(f"Результат деления двух клеток: {cell_1 // cell_2}")
print('-' * 35)
print(cell_1.make_order(1))
print('-' * 35)
print(cell_2.make_order(2))
