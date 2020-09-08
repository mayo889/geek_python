from random import randint

arr = [randint(1, 30) for i in range(20)]
print(f"Исходный список:\n{arr}")
new_arr = [el for el in arr if arr.count(el) == 1]
print(f"Элементы списка, не имеющие повторений:\n{new_arr}")
