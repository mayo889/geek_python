from googletrans import Translator

translate_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

file_in = open('text_4.txt', encoding="utf-8")

# Вариант решения через словарь
with open('text_4_result_1.txt', 'w', encoding="utf-8") as file_out:
    for line in file_in:
        elem = line.split()
        elem[0] = translate_dict[elem[0]]
        file_out.write(' '.join(elem) + '\n')

# Вариант решения через Google Translate API
with open('text_4_result_2.txt', 'w', encoding="utf-8") as file_out_2:
    translator = Translator()
    file_in.seek(0)
    for line in file_in:
        file_out_2.write(translator.translate(line, src='en', dest='ru').text + '\n')

file_in.close()
