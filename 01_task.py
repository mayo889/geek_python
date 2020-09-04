def main_func():
    a = float(input('Введите делимое: '))
    b = float(input('Введите делитель: '))

    def sum_func(x, y):
        try:
            print(f"{x / y:.3f}")
        except ZeroDivisionError:
            print('Вы пытаетесь поделить на ноль!')

    sum_func(a, b)
    print('Напишите "да", чтобы повторить ввод чисел, или "нет", чтобы окончить программу')
    ans = input('Ответ: ')
    if ans == 'да':
        main_func()
    elif ans == 'нет':
        print('Программа завершена')
    else:
        print('Вы ввели неккоректный ответ. Программа завершена')


main_func()
