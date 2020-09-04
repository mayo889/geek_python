def check_latin(word):
    if not word.islower():
        return False
    for letter in word:
        if not (97 <= ord(letter) <= 122):
            return False
    return True


def int_func(arr):
    errors = []
    for i in range(len(arr)):
        if check_latin(arr[i]):
            arr[i] = arr[i].capitalize()
        else:
            errors.append(arr[i])
    print("Данные слова были введены неправильно и были проигнорированы программой: ", *errors)
    print("Полученная строка: ", *arr)


arr = list(input('Введите строку слов из латинских букв в нижнем регистре: ').split())
int_func(arr)