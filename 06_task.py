school = {}

with open("text_6.txt", encoding="utf-8") as file:
    for line in file:
        line = line.split()
        subject = line[0][:-1]
        hours = 0
        for elem in line[1:]:
            if elem != '-':
                hours += int(elem[:elem.index('(')])
        school[subject] = hours

print(school)
