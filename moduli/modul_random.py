# ''' Орел & Решка '''
#
# import random
#
# n = int(input())    # количество попыток
# for i in range(n):
#     li = random.choice(['Орел', 'Решка'])
#     print(li)

# ''' or '''
#
# import random
# print(*[("Орел","Решка")[random.randint(0,1)] for i in range(int(input()))], sep = '\n')
#
#
# ''' or '''
#
# from random import randint
#
# COIN = ['Орел', 'Решка']
#
# for _ in range(int(input())):
#     print(COIN[randint(0, 1)])


# ''' моделирует броски игрального кубика c 6 гранями '''
#
# import random
#
# for i in range(int(input())):
#     num = random.randint(1, 6)
#     print(num)


# ''' or '''
#
# from random import randrange as rr
# [print(rr(1, 7)) for _ in range(int(input()))]


# ''' генерирует случайный пароль '''
#
# from random import choice
#
# def generate_password(length):
#     start_upper = 65  # Начальный код символа Uppercase (A)
#     end_upper = 90    # Конечный код символа Uppercase (Z)
#     start_lower = 97  # Начальный код символа Lowercase (a)
#     end_lower = 122   # Конечный код символа Lowercase (z)
#
#     all_characters = [chr(code) for code in range(start_upper, end_upper + 1)] + [chr(code) for code in range(start_lower, end_lower + 1)]
#
#     return ''.join([choice(all_characters) for _ in range(length)])
#
# length = int(input())  # длина пароля
# password = generate_password(length)
# print(password)
# #
#
#
# ''' or '''
#
# from random import *
#
# for _ in range(int(input())):
#     print(chr(choice([randint(65, 90), randint(97, 122)])), end='')
#
#
# ''' or '''
#
# import random
#
# length = int(input())    # длина пароля
#
# for _ in range(length):
#     if random.randint(0, 1):
#         print(chr(random.randint(65, 90)), end='')
#     else:
#         print(chr(random.randint(97, 122)), end='')
#
#
# ''' or '''
#
# from random import randint as R
#
# for _ in range(int(input())):
#     print([chr(R(65, 90)), chr(R(97, 122))][R(0, 1)], end = '')

# ''' Генерирует 7 различных случайных чисел, числа не содержат дубликатов. '''
#
# import random
#
# results = []
# for i in range(int(input())):
#     result = random.randint(1, 49)
#     results.append(result)
#
# sorted_results = sorted(results)
# print(*sorted_results)
#
#
# ''' or '''
#
# import random
#
# s = set()
# while len(s) < 7:
#     s.add(random.randint(1, 49))
# print(*sorted(s))
#
#
# ''' or '''
#
# import random as rnd
# print(*sorted(rnd.sample(range(1, 50), 7)))


# ''' IP адрес состоит из четырех чисел из диапазона от 0 до 255 (включительно) разделенных точкой.'''
#
# import random
# def generate_ip():
#     ip = f'{random.randrange(256)}.{random.randrange(256)}.{random.randrange(256)}.{random.randrange(256)}'
#     print(ip)
#
# generate_ip()
#
#
# ''' or '''
#
# from random import randrange as r
#
# def generate_ip():
#     return f'{r(256)}.{r(256)}.{r(256)}.{r(256)}'
#
#
# ''' or '''
#
# from random import choice
#
#
# def generate_ip():
#     return '.'.join(str(choice(range(256))) for _ in range(4))
#
#
#
# ''' or '''
#
# from random import randint
#
# def generate_ip():
#     return f'{randint(0, 255)}.{randint(0, 255)}.{randint(0, 255)}.{randint(0, 255)}'


# ''' Post code generation '''
#
# from random import *
#
#
# def generate_index():
#     return (f'{chr(randint(65, 90))}{chr(randint(65, 90))}{randrange(100)}_{randrange(100)}'
#             f'{chr(randint(65, 90))}{chr(randint(65, 90))}')
#
#
# print(generate_index())
#
# ''' or '''
#
# from random import choice, randint
# from string import ascii_uppercase as letter
#
#
# def generate_index():
#     return (f'{choice(letter)}{choice(letter)}{randint(0, 99)}_{randint(0, 99)}'
#             f'{choice(letter)}{choice(letter)}')
#
#
# ''' or '''
#
# from random import choice, randrange
# from string import ascii_uppercase
#
#
# def generate_index():
#     n1, n2 = (randrange(100) for i in range(2))
#     a, b, c, d = (choice(ascii_uppercase) for i in range(4))
#     return (f'{a}{b}{n1}_{n2}{c}{d}')
#
#
# ''' or '''
#
# from random import randint
#
#
# def generate_index():
#     return (f'{chr(randint(65, 90)) * 2}{randint(0, 99)}_{randint(0, 99)}'
#             f'{chr(randint(65, 90)) * 2}')



# ''' перемешивает случайным образом содержимое матрицы '''
#
#
# from random import *
#
# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]
#
# def generate_ip():
#     shuffle(matrix)
#     return matrix
#
#
# print(generate_ip())


# ''' tickets generator '''
#
# import random
# print(*random.sample(range(1000000, 10000000), 100), sep='\n')
#
#
# ''' or '''
#
# from random import *
# import string
#
# num = [i for i in range(1, 9)]
# for i in range(1, 101):
#     print(*sample(num, 7), sep='')



# ''' Анаграмма '''
#
#
# from random import *
#
# word = input()
#
# characters = [char for char in word]
# shuffle(characters)
# new_string = ''.join(characters)
# print(new_string)
#
#
# ''' or '''
#
# from random import sample as S
#
# anagram = input()
#
# print(''.join(S(anagram, len(anagram))))
#
#
# ''' or '''
#
# import random as r
# w = list(input())
# r.shuffle(w)
# print(*w, sep='')



# ''' Игро в Бинго '''
#
#
# from random import *
#
#
# num = [i for i in range(1, 76)]
# numbers = sample(num, 25)
# bingo = [[str(numbers.pop()).ljust(3) for _ in range(5)] for _ in range(5)]
# bingo[2][2] = str(0).ljust(3)
# [print(*row, sep='') for row in bingo]
#
#
# ''' or '''
#
# from random import sample
#
# bingo = sample(range(1, 76), 24)
# bingo.insert(12, 0)
# for i in range(5):
#     for j in range(5):
#         print(str(bingo[i * 5 + j]).rjust(3), end='')
#     print()
#
#
# ''' or '''
#
# from random import shuffle
#
#
# lst = list(range(1, 76))
# shuffle(lst)
# m = [[lst.pop() for _ in range(5)] for _ in range(5)]
# m[2][2] = 0
# for row in m:
#     print(*row)
#
#
# ''' or '''
#
# from random import sample
#
# numbers = sample(range(1, 76), 25)
# bingo = [numbers[i:i + 5] for i in range(0, 21, 5)]
# bingo[2][2] = 0
#
# for i in range(5):
#     for j in range(5):
#         print(str(bingo[i][j]).ljust(3), end=' ')
#     print()



# ''' Тайный друг 🌶️ '''
#
# stud_quantity = int(input())
# list_of_students = []
# for i in range(stud_quantity):
#     students = input()
#     list_of_students.append(students)
#
# for i in range(len(list_of_students)):
#     print(f'{list_of_students[i]} - {list_of_students[(i + 1) % len(list_of_students)]}')
#
#
#
# ''' or '''
#
# import random
#
# S = [input() for _ in range(int(input()))]
# random.shuffle(S)
#
# for i in range(1, len(S) + 1):
#     if i == len(S):
#         print(f'{S[i - 1]} - {S[0]}')
#     else:
#         print(f'{S[i - 1]} - {S[i]}')


# ''' Генератор паролей 1 '''
#
# from random import *
# from string import *
#
# letter = (set(ascii_letters) | set(digits)) - set('lI1oO0')
#
#
# def generate_password(length):
#     result = ''.join(choice(list(letter)) for _ in range(length))
#     return result
#
#
# def generate_passwords(count, length):
#     for i in range(count):
#         print(generate_password(length))
#
# n, m = int(input()), int(input())
#
# generate_passwords(n, m)
#
#
# ''' or '''
#
# import random
# import string
#
# s = ''.join((set(string.ascii_letters) | set(string.digits)) - set('lI1oO0'))
# n, m = int(input()), int(input())
# for i in range(n):
#     print(''.join(random.sample(s,m)))


# ''' Генератор паролей 2 🌶️ '''
#
# from random import choice
# from string import ascii_letters, digits
#
# letter = {
#     'EN': [x for x in ascii_letters if x.isupper() and x not in 'OI'],
#     'en': [x for x in ascii_letters if x.islower() and x not in 'ol'],
#     'dig': [x for x in digits if x not in '01']
# }
#
# def generate_password(length):
#     if length < 3:
#         raise ValueError("Password length must be at least 3")
#
#     password = []
#     password.append(choice(letter['EN']))
#     password.append(choice(letter['en']))
#     password.append(choice(letter['dig']))
#
#     for _ in range(length - 3):
#         char_set = choice(list(letter.keys()))
#         password.append(choice(letter[char_set]))
#
#     return ''.join(password)
#
# def generate_passwords(count, length):
#     for i in range(count):
#         print(generate_password(length))
#
# n = int(input("Enter the number of passwords: "))
# m = int(input("Enter the length of passwords: "))
#
# generate_passwords(n, m)
#
#
# ''' or '''
#
# import string
# from random import choice, shuffle
#
# chars1 = [с for с in string.ascii_uppercase if с not in 'OI']
# chars2 = [с for с in string.ascii_lowercase if с not in 'ol']
# chars3 = list(string.digits[2:])
# chars = chars1 + chars2 + chars3
#
# def generate_password(length):
#     result = [choice(i) for i in (chars1, chars2, chars3)] + [choice(chars) for _ in range(3, length)]
#     shuffle(result)
#     return ''.join(result)
#
# def generate_passwords(count, length):
#     result = set()
#     while len(result) < count:
#         result.add(generate_password(length))
#     return list(result)
#
# for i in generate_passwords(int(input()), int(input())):
#     print(i)
#
#
#
# ''' or '''
#
#
# import string
# from random import sample, shuffle
#
# set1 = set('23456789')
# set2 = set(string.ascii_uppercase) - set('IO')
# set3 = set(string.ascii_lowercase) - set('lo')
# n, m = int(input()), int(input())
# for _ in range(n):
#     password = sample(set1, 1) + sample(set2, 1) + sample(set3, 1) + sample(set1|set2|set3, m-3)
#     shuffle(password)
#     print(''.join(password))



# ''' Монте-Карло вычисляет площадь фигуры '''
#
#
# import random
#
# n = 10 ** 6
# k = 0
# s0 = 16
# for _ in range(n):
#     x = random.uniform(-2, 2)
#     y = random.uniform(-2, 2)
#
#     if -2 <= x <= 2 and -2 <= y <= 2 and x**3 + y**4 + 2 >= 0 and x*3 + y**2 <= 2:
#         k += 1
#
# print((k/n)*s0)
#
#
#
#
# ''' при помощи метода Монте-Карло определяет приближённое значение числа π '''
#
# import random
#
# n = 10 ** 6
# S = 4
# k = 0
#
# for _ in range(n):
#     x = random.uniform(-1, 1)
#     y = random.uniform(-1, 1)
#     if x ** 2 + y ** 2 <= 1:
#         k += 1
#
# print((k / n) * S)


# ''' принимает два обязательных аргумента a и b
# и возвращает случайное целое число из отрезка [a;b].'''
#
# import random
#
# num1 = random.randint(0, 17)
# num2 = random.randint(-5, 5)
#
# print(num1)
# print(num2)


# ''' выводит 10 случайных целых чисел из диапазона [1;100]: '''
#
# import random
#
# for _ in range(10):
#     print(random.randint(1, 100))


# import random
#
# print('Бросаем кубики... ')
# print('Значения граней:')
# print(random.randint(1, 6))
# print(random.randint(1, 6))


# import random
#
# again = 'д'
# while again.lower() == 'д':
#     print('Бросаем кубики... ')
#     print('Значения граней:')
#     print(random.randint(1, 6))
#     print(random.randint(1, 6))
#     again = input('Бросить кубики еще раз? (д = да, н = нет): ')


# import random
#
# for _ in range(10):
#     num = random.randint(0, 1)
#     if num == 0:
#         print('Орел')
#     else:
#         print('Решка')


# ''' принимает список в качестве обязательного аргумента и перемешивает его случайным образом. '''
#
# import random
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# random.shuffle(numbers)
# print(numbers)


# ''' принимает список (строку) в качестве обязательного аргумента
# и возвращает один случайный элемент из переданного списка (строки).'''
#
#
# import random
#
# print(random.choice('BEEGEEK'))
# print(random.choice([1, 2, 3, 4]))
# print(random.choice(['a', 'b', 'c', 'd']))


# ''' принимает два обязательных аргумента: список (строку) и количество случайных элементов,
# а возвращает список случайных элементов в указанном количестве. '''
#
# import random
#
# numbers = [2, 5, 8, 9, 12]
#
# print(random.sample(numbers, 1))
# print(random.sample(numbers, 2))
# print(random.sample(numbers, 3))
# print(random.sample(numbers, 5))


# ''' проект угадайка '''
#
# from random import *
#
# # Generate a random number between 1 and 100
# target_number = randint(1, 100)
#
# # Initialize the player's guess
# while True:
#     n = int(input("Введите число от 1 до 100: "))  # Use the same variable 'n' for the player's guess
#
#     if n > target_number:
#         print("Слишком много")
#     elif n < target_number:
#         print("Слишком мало")
#     else:
#         print('Вы угадали, поздравляем!')
#         break  # Exit the loop when the player guesses correctly


# ''' проект угадайка '''
#
# from random import *
#
# # алгоритм игры
# def guessing_game(x, y):
#     phrases_too_much = ['Ох, слишком много! Попробуй еще раз', 'Многовато будет!', 'Ого-го, это слишком много!',
#                         'Много!', 'Бери ниже', 'Многовато!', 'Нужно меньшее число!']
#     phrases_too_little = ['Ох, слишком мало! Попробуй еще раз', 'Маловато будет!', 'Эх, это слишком мало!',
#                         'Мало!', 'Бери выше', 'Маловато!', 'Нужно большее число!']
#     phrases_almost = ['Почти угадал!', 'Горячо, но не очень', 'Уже рядом', 'Ты близок', 'Ты уже рядом', 'Ну же, почти',
#                       'Горячо!']
#     phrases_guessed = ['Поздравляю! Ты угадал моё число :)', 'Молодец! Ты угадал :)', 'Ура, ты угадал! :)']
#     phrases_too_soon = ['Ого, так быстро!', 'Да ты волшебник! Ты угадал моё число', 'Скажи честно, ты подглядывал?',
#                         'У тебя отличная интуиция!', 'Даже я бы не смог отгадать так быстро!']
#     if x > y:
#         x, y = y, x
#         num_0 = randint(x, y)
#         print('Я загадал число от', x, 'до', y, 'Попробуй угадать!')
#     else:
#         num_0 = randint(x, y)
#         print('Я загадал число от', x, 'до', y, 'Попробуй угадать!')
#     count = 0
#     while True:
#         num_1 = int(input())
#         count += 1
#         if num_1 == num_0:
#             if count == 1:
#                 print('Скажи честно, ты подглядывал?')
#                 if input('Хочешь сыграть еще раз? Введи "да" или "нет" ').lower() in ['да', 'lf']:
#                     start()
#                 else:
#                     print('Приходи, когда появится желание сыграть снова :)')
#                     break
#             elif 1 <= count <= 5:
#                 print(choice(phrases_too_soon))
#                 if input('Хочешь сыграть еще раз? Введи "да" или "нет" ').lower() in ['да', 'lf']:
#                     start()
#                 else:
#                     print('Приходи, когда появится желание сыграть снова :)')
#                     break
#             else:
#                 print(choice(phrases_guessed))
#                 if input('Хочешь сыграть еще раз? Введи "да" или "нет" ').lower() in ['да', 'lf']:
#                     start()
#                 else:
#                     print('Приходи, когда появится желание сыграть снова :)')
#                     break
#         elif num_1 > num_0:
#             if abs(num_1 - num_0) < 5:
#                 print(choice(phrases_too_much), choice(phrases_almost), sep='\n')
#             else:
#                 print(choice(phrases_too_much))
#         elif num_1 < num_0:
#             if abs(num_1 - num_0) < 5:
#                 print(choice(phrases_too_little), choice(phrases_almost),  sep='\n')
#             else:
#                 print(choice(phrases_too_little))
#
# # описание правил
# def game_rules():
#     print('Отлично! Давай ознакомлю тебя с правилами игры.')
#     print('Я загадаю число, а ты будешь его отгадывать.')
#     print('Диапазон чисел ты выберешь сам.')
#     print('К примеру, если ты укажешь диапазон чисел от 0 до 100, я не смогу загадать число "101" :)')
#     print('Я попрошу тебя ввести границы диапазона. Границы не должны совпадать! Так играть мы не сможем.')
#     input('А теперь напиши что-нибудь, чтобы я был уверен, что ты понял правила игры :)')
#
# # проверка правильности
# def is_valid_x(x):
#     if x.isdigit() is False:
#         print('Ты ввел не число :(')
#         print('Что ж, ладно, введи новые числа.')
#         start()
#
# def is_valid_xy(x, y):
#     while x == y:
#         print('Ты ввел одинаковые числа. Я же говорил, что так играть мы не сможем :(')
#         print('Что ж, ладно, введи новое число.')
#         start()
#     if y.isdigit() is False:
#         print('Я запутался :( Это не число')
#         print('Давай заново :)')
#         start()
#     else:
#         return True
#
# # запуск игры
# def start():
#     x = input('Введи первую границу диапазона: ')
#     is_valid_x(x)
#     y = input('Введи вторую границу диапазона: ')
#     if is_valid_xy(x, y) is True:
#         x, y = int(x), int(y)
#         guessing_game(x, y)
#
# # приглашение в игру
# if input('Приветствую тебя в программе Дмитрия! Не желаешь сыграть в игру? Введи "да" или "нет" ').lower() in ['да', 'lf']:
#     game_rules()
#     start()
# else:
#     if input('Это не займёт много времени и сил. Если всё таки надумал, введи "да" :)').lower() in ['да', 'lf']:
#         game_rules()
#         start()
#     else:
#         print('Приходи, когда появится желание сыграть :)')


# ''' Угадай число '''
#
# from math import *
# from math import ceil
# right = int(input())
# b = 2
# def logo():
#     res = log(right, b)
#     print(int(ceil(res)))
#
# logo()
#
# ''' or '''
#
# from math import log2, ceil
# print (ceil(log2(int(input()))))
#
#
# ''' or '''
#
# n = int(input())
# attempts = 0
#
# while 2 ** attempts < n:
#     attempts += 1
#
# print(attempts)
