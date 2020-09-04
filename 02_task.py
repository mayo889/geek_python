def func_info(**kwargs):
    print(
        f"Пользователь {kwargs['name']} {kwargs['surname']} родился в {kwargs['data']} году. "
        f"В данный момент проживает в городе {kwargs['city']}. Контактные данные. "
        f"email: {kwargs['email']}, номер телефона: {kwargs['telephone']}.")


func_info(name=input('Введите имя: '), surname=input('Введите фамилию: '), data=input('Введите год рождения: '),
          city=input('Введите город проживания: '), email=input('Введите mail: '),
          telephone=input('Введите номер телефона: '))
