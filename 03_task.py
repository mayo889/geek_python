class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt


arr = []
print("Вводите числа через enter или q для окончания программы.")
while True:
    elem = input()
    if elem == "q":
        print(*arr)
        break
    try:
        if not elem.isdigit():
            raise MyException("Вы ввели не число! Вы можете продолжить ввод чисел.")
    except MyException as err:
        print(err.txt)
    else:
        arr.append(int(elem))
