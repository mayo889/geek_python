goods = []

template_dict = {
    "название": None,
    "цена": None,
    "количество": None,
    "ед": None
}

while True:
    print('Чтобы добавить товар, напишите: добавить')
    print('Чтобы получить аналитику, напишите: аналитика')
    ans = input('Ответ: ')
    if ans == 'добавить':
        goods.append((len(goods) + 1, template_dict.copy()))
        for name in template_dict:
            value = input(f'Введите {name}: ')
            if value.isdigit():
                value = int(value)
            goods[len(goods) - 1][1][name] = value
    elif ans == 'аналитика':
        break
    else:
        print('Такого варианта ответа нет, попробуйте еще раз')

print('Готовая структура данных \"Товары\"')
for i in range(len(goods)):
    print(goods[i])

analysis = {
    "название": [],
    "цена": [],
    "количество": [],
    "ед": []
}

for i in range(len(goods)):
    for name in template_dict:
        analysis[name].append(goods[i][1][name])

print('Собранная аналитика данных \"Товары\"')
for elem, value in analysis.items():
    print(f"{elem:>10}:", end=' ')
    for i in value:
        print(f'{str(i):<20}', end=' ')
    print('')
