nick_1 = 'Ben'
pass_1 = 'qwerty'
nick_2 = 'Mike'
pass_2 = 'zxcvb'

nick = input('Введите свой никнейм: ')
password = input('Введите свой пароль: ')

if (nick == nick_1 and password == pass_1) or (nick == nick_2 and password == pass_2):
    print('Вход в профиль успешно выполнен')
elif nick != nick_1 and nick != nick_2:
    print('Неправильный никнейм')
else:
    print('Неправильный пароль')