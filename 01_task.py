from sys import argv


def salary(hours, rate, prize):
    return hours * rate + prize


try:
    path, hours, rate, prize = argv
    hours, rate, prize = float(hours), float(rate), float(prize)
    print(f"Заработная плата сотрудника составит: {salary(hours, rate, prize)}")
except ValueError:
    print("Вы запустили скрипт расчета заработной платы с неправильными параметрами.")
    print("Необходимо ввести значение выработки в часах, ставку в час и значение премии через пробел")
