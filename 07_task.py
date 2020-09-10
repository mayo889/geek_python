import json

company = {}

with open("text_7.txt", encoding="utf-8") as file:
    all_profit = 0
    num = 0
    for line in file:
        line = line.split()
        profit = int(line[2]) - int(line[3])
        company[line[0]] = profit
        if profit > 0:
            all_profit += profit
            num += 1

with open("text_7_result.json", "w", encoding="utf-8") as file:
    json.dump([company, {"average_profit": all_profit / num}], file, ensure_ascii=False, indent=4)
