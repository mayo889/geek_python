from random import randint

arr = [randint(1, 300) for i in range(15)]
print(f"Исходный список:\n{arr}")
new_arr = [arr[i] for i in range(1, len(arr)) if arr[i] > arr[i - 1]]
print(f"Элементы исходного списка, значения которых больше предыдущего элемента:\n{new_arr}")
