from itertools import count, cycle

start_digit = int(input('Введите число, начиная с которого сгенерировать список до 15: '))
x = count(start_digit)
for i in range(15 - start_digit + 1):
    print(next(x), end=' ')
print()

arr = ['Python', 'C++', 'Pascal', 'Java', 'Go']
y = cycle(arr)
amount = int(input(f'Сколько раз вывести элементы списка {arr}: '))
for i in range(amount):
    print(next(y))
