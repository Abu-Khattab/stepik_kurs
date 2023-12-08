''' exemple '''

from random import *

''' Предпоследняя строка '''

x = open(input(), 'r', encoding='utf-8')
content = x.readlines()[-2]
print(content)
x.close()


''' Случайная строка '''

x = open(r'/Users/user/stepik_kurs/rabota_s_files/tests.txt', 'r', encoding='utf-8')
content = x.readlines()
print(choice(content))
x.close()


''' Сумма двух-1 '''

file = open('numbers.txt', encoding='utf-8')
res = sum(map(int, file))
print(res)
file.close()

''' or '''

print(sum(map(int, open('numbers.txt'))))

''' or '''

l = [int(i) for i in open('numbers.txt')]
print(sum(l))


''' Сумма двух-2 '''

x = open(r'/Users/user/stepik_kurs/rabota_s_files/tests.txt', 'r', encoding='utf-8')
x1 = [int(i) for i in x.read().split()]
print((sum(x1)))

''' or '''

print(sum(map(int, open('numbers.txt').read().split())))

''' or '''

file = open('nums.txt')
print(sum(map(int, file.read().split())))
file.close()

''' Общая стоимость '''

file = open('prices.txt')
summ = 0
for line in file:
    product = line.split()
    summ += int(product[1]) * int(product[2])
print(summ)
file.close()


''' or '''

file = open('prices.txt')
lines = map(str.split, file)
print(sum(map(lambda line: int(line[1]) * int(line[2]), lines)))
file.close()


''' or '''

file = open('prices.txt', 'r', encoding='utf-8')
s = 0
for line in file:
    tovar, count, price = line.split()
    s += int(count) * int(price)
print(s)
file.close()


''' Переворот строки '''

with open(r'/Users/user/stepik_kurs/rabota_s_files/tests.txt', encoding='utf-8') as file:
    line1 = file.readline().strip()
    rever = ''.join(reversed(line1))
    print(rever)

''' or '''

with open('text.txt') as f:
    print(f.read()[::-1])

''' or '''

with open('text.txt', 'r', encoding = 'utf-8') as f:
    print(f.read().strip()[::-1])


''' or '''

with open('text.txt', encoding='utf-8') as file:
    print(file.readline().rstrip()[::-1])


''' Обратный порядок '''

with open(r'/Users/user/stepik_kurs/rabota_s_files/tests.txt', encoding='utf-8') as file:
    lines = file.readlines()
    for line in reversed(lines):
        print(line.strip())

''' or '''

with open('data.txt', encoding='utf-8') as file:
    print(*file.readlines()[::-1], sep='')

''' or '''

with open('data.txt', encoding='UTF-8') as file:
    for i in file.readlines()[::-1]:
        print(i.strip())


''' Длинные строки '''

with open(r'/Users/user/stepik_kurs/rabota_s_files/tests.txt', encoding='utf-8') as file:
    s = len(max(file.readlines(), key=len))
    li = []
    file.seek(0)
    for line in file:
        if len(line) == s:
            li.append(line)
    lis = ''.join(li)
    print(lis.strip())


''' or '''

with open('lines.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    longest = max(map(len, lines))
    print(*filter(lambda x: len(x) == longest, lines), sep='\n')


''' or '''

with open('lines.txt', encoding='utf-8') as file:
    text = file.readlines()

n = len(max(text, key=len))
print(*filter(lambda x: len(x) == n, text), sep='')


''' Сумма чисел в строках '''

with open(r'/Users/user/stepik_kurs/rabota_s_files/tests.txt', encoding='utf-8') as file:
    lines = file.readlines()

for line in lines:
    numbers = line.split()
    print(numbers)
    total = sum(int(num) for num in numbers if num.isdigit())
    print(total)


''' or '''

with open('numbers.txt') as f:
    for line in f:
        print(sum(map(int, line.split())))


''' or '''

with open('numbers.txt') as file:
    [print(sum(map(int, i.strip().split()))) for i in file]


''' Сумма чисел в файле '''

import re

sum_total = 0

with open(r'/Users/user/stepik_kurs/rabota_s_files/tests.txt', encoding='utf-8') as file:
    lines = file.readlines()

for line in lines:
    pattern = r'\d+'
    matches = re.findall(pattern, line)

    total = [int(x) for x in matches]
    sum_total += sum(total)
print(sum_total)


''' or '''

import re
with open('nums.txt') as f:
    print(sum(sum(map(int, re.findall(r'\d+', line))) for line in f))


''' or '''
''' Меняем  все символы кроме цифр на пробелы. '''

with open('nums.txt') as file:
    cont = file.read()
    for i in filter(lambda x: not x.isdigit(), cont):
        cont = cont.replace(i, ' ')
    print(sum(map(int, cont.split())))


''' Статистика по файлу '''

import re


def counter_text():

    sum_total = 0

    with open(r'/Users/user/stepik_kurs/rabota_s_files/tests.txt', encoding='utf-8') as file:
        lines = file.readlines()

        # Количество строк
        line_count = len(lines)

        # Преобразование текста в одну строку
        all_text = " ".join(lines)

        # Количество слов
        word_count = len(re.findall(r'\b\w+\b', all_text))

        # Количество букв
        letter_count = len(re.findall(r'[а-яА-Яa-zA-Z]', all_text))

        # Вывод результатов
        print(f"Input file contains:")
        print(f"{letter_count} letters")
        print(f"{word_count} words")
        print(f"{line_count} lines")

counter_text()


''' or '''

with open('lines.txt') as f:
    txt = f.read()
    print('Input file contains:')
    print(sum(map(str.isalpha, txt)), 'letters')
    print(len(txt.split()), 'words')
    print(txt.count('\n') + 1, 'lines')


''' or '''

with open('file.txt') as f:
    t = f.read()
    f.seek(0)
    print('Input file contains:')
    print(f'{len(list(filter(str.isalpha, t)))} letters')
    print(f'{len(t.split())} words')
    print(f'{len(f.readlines())} lines')


''' Random name and surname '''

with open(r'/Users/user/stepik_kurs/rabota_s_files/first_names.txt', encoding='utf-8') as file1, open(r'/Users/user/stepik_kurs/rabota_s_files/last_names.txt', encoding='utf-8') as file2:
    all_members = [(name.strip(), lastname.strip()) for name, lastname in zip(file1, file2)]
    for name, lastname in all_members[:3]:
        print(name, lastname)


''' or '''

import random


with open('first_names.txt', 'r', encoding='utf-8') as f, open('last_names.txt', 'r', encoding='utf-8') as l:
    z, x = f.readlines(), l.readlines()
    for i in range(3):
        print(random.choice(z).strip(), random.choice(x).strip(), sep=' ')


''' or '''

from random import sample
with open('first_names.txt') as name, open('last_names.txt') as surname:
    names = sample(name.read().split(), 3)
    surnames = sample(surname.read().split(), 3)
    for i in range(3):
        print(names[i], surnames[i])



''' Необычные страны '''

with open(r'/Users/user/stepik_kurs/rabota_s_files/population.txt', encoding='utf-8') as file:
    all_members = [line.strip().split('\t') for line in file]
    res = [line for line in all_members if line[0][0] == 'G' and int(line[-1]) > 500000]
    for line in res:
        print('\t'.join(line))


''' or '''

with open(r'/Users/user/stepik_kurs/rabota_s_files/population.txt', encoding='utf-8') as file:
    all_members = [line.strip().split('\t') for line in file]
    res = [line for line in all_members if line[0][0] == 'G' and int(line[-1]) > 500000]
    for line in res:
        print(line[0])


''' or '''

with open('population.txt') as f:
    for line in f:
        n, p = line.split('\t')
        if n.startswith('G') and int(p) > 500000:
            print(n)


''' CSV-файл '''

def read_csv():
    with open('data.csv') as file:
        keys = file.readline().strip().split(',')
        return [dict(zip(keys, line.strip().split(','))) for line in file]


''' or '''

import csv


def read_csv():
    data = []

    with open(r'/Users/user/stepik_kurs/rabota_s_files/data.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            data.append(row)

    return data

print(read_csv())


''' or '''

import csv


def read_csv():
    with open('data.csv') as csv_file:
        reader = csv.DictReader(csv_file)
        return [row for row in reader]


'''  Входная строка '''

with open(r'/Users/user/stepik_kurs/rabota_s_files/output.txt', 'w') as file:
    print('Позвоните нам: (916) 928-92xx\n', file=file)

''' or '''

with open(r'/Users/user/stepik_kurs/rabota_s_files/output.txt', 'w') as file:
    print(input(), file=file)



''' Случайные числа '''

import random


lists = [str(random.randint(111, 778)) for x in range(25)]

with open(r'/Users/user/stepik_kurs/rabota_s_files/random.txt', 'w', encoding='utf-8') as file:
    file.writelines('\n'.join(lists))


''' or '''

from random import randrange
with open('random.txt','w') as out:
    print(*[randrange(111,778) for _ in range(25)],sep='\n',file=out)


''' or '''

from random import randint
with open('random.txt', 'w') as f:
    f.writelines([str(randint(111,777))+'\n' for _ in range(25)])


''' or '''

from random import sample as r

print(*r(range(111, 778), 25), file=open('random.txt', 'w'), sep='\n')


''' or '''

import random
with open('random.txt', 'w') as output:
    print(*random.sample(range(111, 777), 25), sep='\n', file=output)


''' Нумерация строк '''


with open(r'/Users/user/stepik_kurs/rabota_s_files/tests.txt', 'r') as f:
    # Читаем все строки и убираем пробелы
    lines = [line.strip() for line in f]

with open(r'/Users/user/stepik_kurs/rabota_s_files/output.txt', 'w', encoding='utf-8') as s:
    # Записываем пронумерованные строки в выходной файл
    s.writelines(f"{index}) {line}\n" for index, line in enumerate(lines, start=1))


''' or '''

with open('input.txt') as inp, open('output.txt', 'w') as out:
    for i, j in enumerate(inp, start=1):
        print(f'{i}) {j}', end='', file=out)


''' or '''

with open('input.txt') as fin, open('output.txt', 'w') as fout:
    [fout.write(f'{i}) {line}') for i, line in enumerate(fin, 1)]


''' Подарок на новый год '''

with open(r'/Users/user/stepik_kurs/rabota_s_files/class_scores.txt', 'r') as f:
    # Читаем строки из файла
    lines = f.readlines()

with open(r'/Users/user/stepik_kurs/rabota_s_files/output.txt', 'w', encoding='utf-8') as s:
    # Обрабатываем каждую строку
    for line in lines:
        # Разделяем фамилию и оценку
        parts = line.split()
        name, score = parts[0], int(parts[1])

        # Увеличиваем оценку на 5 баллов
        new_score = min(score + 5, 100)  # Ограничиваем оценку максимальным значением 100

        # Записываем в новый файл
        s.write(f"{name} {new_score}\n")

    print("Файл new_scores.txt успешно создан.")



''' or '''

with open('class_scores.txt') as i, open('new_scores.txt', 'w') as o:
    for _ in i.readlines():
        n, s = _.split()
        print(f'{n} {min(int(s) + 5, 100)}', file=o)


''' or '''

with open('class_scores.txt') as class_scores, open('new_scores.txt', 'w') as new_scores:
    for line in class_scores:
        name, score = line.split()
        score = int(score) + 5
        if score > 100:
            score = 100
        print(name, score, file=new_scores)



''' Загадка от Жака Фреско 🌶️ '''

with open(r'/rabota_s_files/words2.txt', 'r') as file:
    x = file.read().split('GOATS')
    colors = x[0].split('\n')[1:]
    goats = x[1].split('\n')

with open(r'/Users/user/stepik_kurs/rabota_s_files/output.txt', 'w', encoding='utf-8') as answers:
    for line in colors:
        if goats.count(line) > len(goats) * 0.07:
            answers.write(line + '\n')


''' or '''

with open('words2.txt', 'r') as goats, open('answer.txt', 'w') as out:
    s = goats.read().split('\n')
    [print(i, file=out) for i in sorted(set(s)) if (s.count(i)-1) > 7]




''' Конкатенация файлов 🌶️ '''

input_files_number = int(input())
# здесь мы будем хранить имена всех файлов, из которых нам нужно взять содержимое
input_files = [input() for _ in range(input_files_number)]

with open("output.txt", "w", encoding="utf-8") as output_f:
    for input_file in input_files:  # проходим по всем файлам
        with open(input_file, "r", encoding="utf-8") as input_f:
            file_contents = input_f.read()  # считываем содержимое файла
            output_f.write(file_contents)  # записываем содержимое файла


''' or '''

with open(r'/Users/user/stepik_kurs/rabota_s_files/words.txt', 'r') as words, open(r'/Users/user/stepik_kurs/rabota_s_files/words2.txt', 'r') as words2:
    x2 = words2.read()
    x = words.read()

with open(r'/Users/user/stepik_kurs/rabota_s_files/output.txt', 'w', encoding='utf-8') as output:
    output.write(x + x2)



''' Лог файл 🌶️ '''


def minutes(x):
    res = [int(i) for i in x.split(':')]
    return res[0] * 60 + res[1]



with open(r'/Users/user/stepik_kurs/rabota_s_files/logfile.txt', 'r') as times, open(r'/Users/user/stepik_kurs/rabota_s_files/output.txt', 'w', encoding='utf-8') as output:
    for line in times:
        a, b, c = line.strip().split(', ')
        if minutes(c) - minutes(b) >= 60:
            output.write(a+'\n')


minutes(c)


''' or '''

def get_diff_mins(time2, time1):
    t2 = list(map(int, time2.split(':')))
    t1 = list(map(int, time1.split(':')))
    return (t2[0]*60 + t2[1]) - (t1[0]*60 + t1[1])

with open('logfile.txt', encoding='utf-8') as inputf, open('output.txt', 'w') as outputf:
    for fn in inputf:
        name, time1, time2 = fn.strip().split(', ')
        if get_diff_mins(time2, time1) >= 60:
            print(name, file=outputf)