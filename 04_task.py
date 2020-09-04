def my_func(x, y):
    ans = 1
    y_copy = y
    while y < 0:
        ans *= x
        y += 1
    print(f"Число {x} в степени {y_copy} равняется: {1 / ans:.5f}")


while True:
    a = float(input("Введите действительное положительное число: "))
    if a > 0:
        break
    else:
        print('Вы ввели неккоректное число. Повторите попытку.')

while True:
    b = int(input("Введите целое отрицательное число: "))
    if b <= 0 and b % 1 == 0:
        break
    else:
        print('Вы ввели неккоректное число. Повторите попытку.')

my_func(a, b)
