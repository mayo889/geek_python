x = int(input('Введите целое положительное число: '))
max_num = 0

while x > 0:
    digit = x % 10
    if digit > max_num:
        max_num = digit
    x //= 10

print(f'Самая большая цифра в веденном числе: {max_num}')
