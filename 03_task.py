with open("text_3.txt", encoding="utf-8") as file:
    all_salary = 0
    num = 0
    print("Сотрудники, имеющие оклад менее 20 тыс.:")
    for line in file:
        name, salary = line.split()
        if float(salary) < 20000:
            print(name)
        all_salary += float(salary)
        num += 1
    print(f"Средняя величина дохода всех сотрудников: {all_salary / num}")
