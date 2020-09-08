from functools import reduce

arr = [i for i in range(100, 1001) if i % 2 == 0]
print("Произведение четных чисел от 100 до 1000: ", reduce(lambda prev_el, el: prev_el * el, arr))
