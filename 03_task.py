def my_func(*args):
    return sum(args) - min(args)


a, b, c = map(int, input('Введите три числа через пробел: ').split())
res = my_func(a, b, c)
print(f"Сумма наибольших двух введенных чисел: {res}")
