data_types = [2, 3.14, 2 + 3j, 'Hello', [5, 'World', 5.29], (1, 2, 3), {23, 34, 45}, {'Январь': 1, 'Февраль': 2},
              True, b'bytes', bytearray(b'list_of_bytes'), None]

try:
    raise Exception('raise exception')
except Exception as error:
    data_types.append(error)

print('Типы данных в Python:')
for ind, elem in enumerate(data_types, 1):
    print(f'{ind}. Тип данных {elem} - {type(elem)}')
