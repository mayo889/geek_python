class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    a, b = map(int, input("Введите делимое и делитель через пробел: ").split())
    if b == 0:
        raise MyException("Делить на ноль нельзя!")
except ValueError:
    print("Необходимо ввести числа")
except MyException as err:
    print(err.txt)
else:
    print(f"{a} / {b} = {a / b}")
finally:
    print("Программа окончила работу.")
