my_list = [7, 5, 3, 3, 2]
print('Исходный рейтинг:')
print(*my_list)

while True:
    dig = int(input('Введите новое натуральное число для рейтинга или -1 для окончания программы: '))
    if dig == -1:
        print('Программа завершила работу')
        break
    if my_list.count(dig) >= 1:
        my_list.insert(my_list.index(dig) + my_list.count(dig), dig)
    else:
        copy_dig = dig - 1
        while my_list.count(copy_dig) == 0 and copy_dig > 0:
            copy_dig -= 1
        if copy_dig == 0:
            my_list.append(dig)
        else:
            my_list.insert(my_list.index(copy_dig), dig)
    print("Результат: ", *my_list)
