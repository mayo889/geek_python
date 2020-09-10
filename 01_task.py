with open("text_1.txt", 'w', encoding="utf-8") as file:
    print("Напишите текст для записи в файл или пустую строку для окончания записи:")
    while True:
        text = input()
        if text == '':
            break
        file.write(text + '\n')
