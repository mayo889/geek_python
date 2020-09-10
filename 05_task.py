from random import randint

with open("text_5.txt", 'w', encoding="utf-8") as file:
    file.writelines(' '.join([str(randint(-5, 10)) for _ in range(10)]))

with open("text_5.txt", encoding="utf-8") as file:
    print(sum(list(map(int, file.readline().split()))))
