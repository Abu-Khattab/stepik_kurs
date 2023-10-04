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


