line = input('Введите строку из нескольких слов, разделенных пробелами: ').split()

for ind, elem in enumerate(line, 1):
    print(f'{ind}. {elem[:10]}')
