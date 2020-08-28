x = input('Введите число: ')

print('Первый способ:')
print(int(x) + int(x * 2) + int(x * 3))

print('*' * 25)

length = len(x)
x = int(x)

print('Второй способ:')
a = x
b = x * 10 ** length + x
c = x * 100 ** length + x * 10 ** length + x
print(a + b + c)

print('*' * 25)

print('Третий способ:')
a = x * 100 ** length
b = x * 2 * 10 ** length
c = x * 3
print(a + b + c)
