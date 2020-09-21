class MyException(Exception):
    pass


class Data:
    def __init__(self, data):
        try:
            if Data.validation(Data.change(data)):
                self.day, self.month, self.year = Data.change(data)
            else:
                raise MyException()
        except (MyException, Exception):
            print("Неправильный формат даты!")
            exit()

    def __str__(self):
        return f"День: {self.day}. Месяц: {self.month}. Год: {self.year}."

    @classmethod
    def change(cls, data):
        return int(data[0:2]), int(data[3:5]), int(data[6:])

    @staticmethod
    def validation(data):
        return True if (1 <= data[0] <= 31 and 1 <= data[1] <= 12 and 1 <= data[2] <= 9999) else False


date_1 = Data(input("Введите дату в формате dd-mm-yyyy: "))
print(date_1)
