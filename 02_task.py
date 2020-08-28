time = int(input('Введите время в секунах: '))

hours = time // 3600
mins = time % 3600 // 60
sec = time % 3600 % 60

print(f'{hours:0>2d}:{mins:0>2d}:{sec:0>2d}')
