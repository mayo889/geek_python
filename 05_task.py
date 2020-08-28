proceeds = int(input('Введите значение выручки фирмы: '))
costs = int(input('Введите значение издержок фирмы: '))

if proceeds > costs:
    print('Фирма работает в прибыль')
    profit = proceeds - costs
    print(f'Рентабельность выручки: {profit / proceeds * 100:.2f} %')
    count = int(input('Введите количество сотрудников фирмы: '))
    print(f'Прибыль в расчете на одного сотрудника: {profit / count:.3f}')
elif proceeds < costs:
    print('Фирма работает в убыток')
else:
    print('Фирма работает в ноль')
