with open("text_2.txt", encoding="utf-8") as file:
    file.seek(0)
    for num, line in enumerate(file, 1):
        print(f"В {num} строке {len(line.split())} слов.")