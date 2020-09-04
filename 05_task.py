def get_sum(arr):
    global total
    amount = 0
    for elem in arr:
        try:
            amount += int(elem)
        except ValueError:
            if elem == 'q':
                total += amount
                return amount, 'quit'
            else:
                continue
    total += amount
    return amount, 'ok'


total = 0
print('Для выхода из программы введите символ "q" в любом месте. Иные символы или слова будут игнорироваться!')
while True:
    arr = list(input('Введите числа через пробел: ').split())
    amount, status = get_sum(arr)
    print(f"Сумма введеных чисел: {amount}. Общая сумма введенных чисел: {total}")
    if status == 'quit':
        print('Программа завершила свою работу')
        break
