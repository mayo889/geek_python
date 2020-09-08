def fact(n):
    ans = 1
    for i in range(1, n + 1):
        ans *= i
        yield f'{i}! = {ans}'


n = int(input('Введите число, до которого необходимо найти факториалы: '))
for el in fact(n):
    print(el)
