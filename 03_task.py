class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


worker_1 = Position('Ivan', 'Ivanov', 'Data scientist', 110000, 30000)

print(f"Worker name: {worker_1.name}")
print(f"Worker surname: {worker_1.surname}")
print(f"Worker position: {worker_1.position}")
print(f"Worker wage: {worker_1._income['wage']}")
print(f"Worker bonus: {worker_1._income['bonus']}")
print('*' * 35)
print(f"Worker full name: {worker_1.get_full_name()}")
print(f"Income including premium: {worker_1.get_total_income()}")
