while True:
    try:
        arr = list(map(int, input('Введите целые числа через пробел: ').split()))
        break
    except ValueError:
        print('Вы ввели неправильные данные!')

for i in range(0, len(arr), 2):
    a = arr.pop(i)
    arr.insert(i + 1, a)

print('Список после обмена значений соседних элементов: ', *arr)
