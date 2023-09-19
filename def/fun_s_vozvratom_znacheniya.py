''' Функция с возвратом значения '''

# # функция перевода градусов Фаренгейта в градусы Цельсия
# def convert_to_celsius(temp):
#     result = (5 / 9) * (temp - 32)
#     return result
#
# # основная программа
# temp = float(input('Bвeдитe количество градусов по Фаренгейту: '))
# celsius = convert_to_celsius(temp)
# print(celsius)  # градусы Цельсия


# ''' принимает в качестве аргумента расстояние в километрах и возвращает расстояние в милях '''
#
# # объявление функции
# def convert_to_miles(km):
#     return num * 0.6214
#
# # считываем данные
# num = int(input())
#
# # вызываем функцию
# print(convert_to_miles(num))



# ''' принимает в качестве аргумента номер месяца и возвращает количество дней в данном месяце. '''
#
#
# # объявление функции
# def get_days(month):
#     m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     return m[num - 1]
#
# # считываем данные
# num = int(input())
#
# # вызываем функцию
# print(get_days(num))
#
#
# ''' или '''
#
# def get_days(month):
#     if month in (1, 3, 5, 7, 8, 10, 12): return 31
#     if month in (4, 6, 9, 11): return 30
#     if month == 2: return 28
#
# num = int(input())
#
# print(get_days(num))



# ''' принимает в качестве аргумента натуральное число и возвращает список всех делителей данного числа. '''
#
# # объявление функции
# def get_factors(num):
#     return [i for i in range(1, n + 1) if n % i == 0]
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(get_factors(n))


# ''' или '''
#
#
# # объявление функции
# def get_factors(num):
#     return [i for i in range(1, num//2 + 1) if num % i == 0] + [num]
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(get_factors(n))


# ''' принимает в качестве аргумента число и возвращает количество делителей данного числа. '''
#
# # объявление функции
# def get_factors(num):
#     res = [i for i in range(1, n + 1) if n % i == 0]
#     return len(res)
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(get_factors(n))


# ''' принимает два аргумента: строку target и символ symbol и возвращает список,
#  содержащий все местоположения этого символа в строке'''
#
# # объявление функции
#
# def find_all(target, symbol):
#     return [i for i in range(len(s)) if s[i] == symbol]
#
# # считываем данные
# s = input()
# char = input()
#
# # вызываем функцию
# print(find_all(s, char))
#
#
#
# ''' или так, быстрее отрабатывает говорят '''
#
# # объявление функции
# def find_all(target, symbol):
#     s = []
#     while symbol in target:
#         s.append(target.find(symbol))
#         target = target.replace(symbol, '1', 1)
#     return s
#
# # считываем данные
# s = input()
# char = input()
#
# # вызываем функцию
# print(find_all(s, char))


# ''' принимает в качестве аргументов два отсортированных по возрастанию списка, состоящих из целых чисел,
#     и объединяет их в один отсортированный список. '''
#
# # объявление функции
# def merge(list1, list2):
#     list1.extend(list2)
#     list1.sort()
#     return sorted(list1)
#
# # считываем данные
# numbers1 = [int(c) for c in input().split()]
# numbers2 = [int(c) for c in input().split()]
#
# # вызываем функцию
# print(merge(numbers1, numbers2))
#
#
# ''' или '''
#
# def merge(list1, list2):
#     return sorted(list1 + list2)
# numbers1 = [int(c) for c in input().split()]
# numbers2 = [int(c) for c in input().split()]
# print(merge(numbers1, numbers2))


# ''' selection sort '''
#
# # объявление функции
# def merge(list1, list2):
#     numbers = numbers1 + numbers2
#     for i in range(len(numbers)):
#         for j in range(i ,len(numbers)):
#             if numbers[i] > numbers[j]:
#                 numbers[j], numbers[i] = numbers[i], numbers[j]
#     return numbers
#
# # считываем данные
# numbers1 = [int(c) for c in input().split()]
# numbers2 = [int(c) for c in input().split()]
#
# # вызываем функцию
# print(merge(numbers1, numbers2))


# ''' Слияние двух отсортированных списков '''
#
# def merge(list1, list2):
#     result = list1 + list2   # создаем результирующий список
#     result.sort()            # сортируем список встроенным методом sort()
#     return result            # возвращаем отсортированный список
#
#
# list1 = [3, 10, 11, 12, 47, 57, 58, 63, 77, 79, 80, 95]
# list2 = [0, 3, 11, 12, 20, 24, 26, 47, 48, 53, 65, 70, 81, 84, 84, 90]
# list3 = merge(list1, list2)  # вызываем функцию слияния двух отсортированных списков
#
# print(list3)

#
# ''' Быстрое слияние двух отсортированных списков в один '''
#
# def quick_merge(list1, list2):
#     result = []
#
#     p1 = 0  # указатель на первый элемент списка list1
#     p2 = 0  # указатель на первый элемент списка list2
#
#     while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
#         if list1[p1] <= list2[p2]:
#             result.append(list1[p1])
#             p1 += 1
#         else:
#             result.append(list2[p2])
#             p2 += 1
#
#     if p1 < len(list1):  # прицепление остатка
#         result += list1[p1:]
#     else:  # иначе прицепляем остаток другого списка
#         result += list2[p2:]
#
#     return result
#
#
# list1 = [3, 10, 11, 12, 47, 57, 58, 63, 77, 79, 80, 95]
# list2 = [0, 11, 12, 20, 24, 26, 47, 48, 53, 65, 70, 81, 84, 84, 90]
# list3 = quick_merge(list1, list2)
# print(list3)





# ''' Быстрое слияние нескольких отсортированных списков в один '''
#
#
# def quick_merge(list1, list2):
#     result = []
#
#     p1 = 0  # указатель на первый элемент списка list1
#     p2 = 0  # указатель на первый элемент списка list2
#
#     while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
#         if list1[p1] <= list2[p2]:
#             result.append(list1[p1])
#             p1 += 1
#         else:
#             result.append(list2[p2])
#             p2 += 1
#
#     if p1 < len(list1):  # прицепление остатка
#         result += list1[p1:]
#     else:  # иначе прицепляем остаток другого списка
#         result += list2[p2:]
#
#     return result
#
# list1 = []
# for _ in range(int(input())):
#     list2 = [int(i) for i in input().split()]
#     result = quick_merge(list1, list2)
#     list1 = result
# print(*list1)
#
#
#
# ''' или '''
#
# n = int(input())
#
# s = []
# x = []
# for i in range(n):
#     s += input().split(' ')
# for i in s:
#     x.append(int(i))
# x.sort()
# print(*x)
#
#
# ''' или '''
#
# def quick_merge(n):
#     s = []
#     for i in range(n):
#         n = [int(i) for i in input().split()]
#         s += n
#     s.sort()
#     return s
#
# n = int(input())
# print(*quick_merge(n))
#
#
# ''' или '''
#
# # Функция перевода строковых элементов списка в числа
# def integer_list(txt):
#     lst = []
#
#     for char in txt:
#         lst.append(int(char))
#     return lst
#
#
# # Функция объединения списков (взята из теории 1 в 1)
# def quick_merge(list1, list2):
#     result = []
#
#     p1 = 0
#     p2 = 0
#
#     while p1 < len(list1) and p2 < len(list2):
#         if list1[p1] <= list2[p2]:
#             result.append(list1[p1])
#             p1 += 1
#         else:
#             result.append(list2[p2])
#             p2 += 1
#
#     if p1 < len(list1):
#         result += list1[p1:]
#     if p2 < len(list2):
#         result += list2[p2:]
#
#     return result
#
#
# # Запрашиваем количество входящих списков
# n = int(input())
#
# # Запрашиваем строку и превращаем её в целочисленный список
# lst1 = integer_list(input().split())
#
# # Создаём второй список из list1 и новой строки, которую так же переводим в целочисленный список
# final_list = quick_merge(lst1, integer_list(input().split()))
#
# # Объединяем два полученных списка и результат присваиваем final_list, чтобы вновь его объединить с новым списком
# for _ in range(n - 2):
#     final_list = quick_merge(final_list, integer_list(input().split()))
#
# # Выводим результат
# print(*final_list)



''' Функции с возвратом булевых значений '''


# ''' принимает в качестве аргументов три натуральных числа, и возвращает значение True
#     если существует невырожденный треугольник '''
#
# # объявление функции
# def is_valid_triangle(side1, side2, side3):
#     if (side1 + side2) > side3 and (side1 + side3) > side2 and (side2 + side3) > side1:
#         return True
#     else:
#         return False
# # считываем данные
# a, b, c = int(input()), int(input()), int(input())
#
# # вызываем функцию
# print(is_valid_triangle(a, b, c))
#
#
# ''' или '''
#
# def is_valid_triangle(*sides):
#     return sum(sides) - max(sides) > max(sides)
#
# # считываем данные
# a, b, c = int(input()), int(input()), int(input())
#
# # вызываем функцию
# print(is_valid_triangle(a, b, c))



# ''' принимает в качестве аргумента натуральное число и возвращает значение True если число является простым и
#     False в противном случае '''
#
# # объявление функции
# def is_prime(num):
#     count = 0
#     for i in range(2, num // 2 + 1):
#         if num % i == 0:
#             count += 1
#     if num == 1:
#         return False
#     if count <= 0:
#         return True
#     else:
#         return False
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(is_prime(n))
#
#
# ''' or '''
#
# # объявление функции
# def is_prime(num):
#     if num == 1:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(is_prime(n))
#
#
# ''' or '''
# ''' Более скоростное решение '''
#
# # объявление функции
# def is_prime(num):
#     if num == 1:
#         return False  # число 1 не является простым
#
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False  # сразу возвращает False, когда находим делитель
#
#     return True
#
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(is_prime(n))



# ''' принимает в качестве аргумента натуральное число num и возвращает
#     первое простое число большее числа num   Next Prime 🌶️🌶️ '''
#
#
# def is_prime(num):
#     count = 0
#     for i in range(2, num // 2 + 1):
#         if num % i == 0:
#             count += 1
#     if num == 1:
#         return False
#     if count <= 0:
#         return True
#     else:
#         return False
#
#
#
#
# объявление функции
# def get_next_prime(num):
#     while is_prime(num + 1) == False:
#         num += 1
#         continue
#     return num + 1
#
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(get_next_prime(n))


# ''' or '''
#
# # объявление функции
# def get_next_prime(num):
#     num += 1
#     for i in range(2, num):
#         if num % i == 0:
#             return get_next_prime(num)
#     return num
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(get_next_prime(n))


# '''  Good password 🌶️   принимает в качестве аргумента строковое значение пароля password и возвращает значение True,
#     если пароль является надежным и False - в противном случае. '''
#
#
# def is_password_good(password):
#     if (len(password) >= 8 and any(c.isupper() for c in password)
#             and any(c.islower() for c in password) and any(c.isdigit() for c in password)):
#         return True
#     else:
#         return False
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_password_good(txt))
#
#
# ''' or '''
#
#
# def is_password_good(password):
#     if len(password) < 8:
#         return False
#     flag1 = False
#     flag2 = False
#     flag3 = False
#     for c in password:
#         if c.isupper():
#             flag1 = True
#         elif c.islower():
#             flag2 = True
#         elif c.isdigit():
#             flag3 = True
#     return flag1 and flag2 and flag3
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_password_good(txt))
#
#
# ''' or '''
#
# def is_password_good(password):
#     upp = [i for i in password if i.isupper()]
#     low = [i for i in password if i.islower()]
#     dig = [i for i in password if i.isdigit()]
#     return all([len(password) >= 8, upp, low, dig])
#
#
# txt = input()
# print(is_password_good(txt))



# ''' принимает в качестве аргументов два слова word1 и word2 и возвращает значение True,
#  если слова имеют одинаковую длину и отличаются ровно в одном символе и False  в противном случае.'''
#
# # объявление функции
# def is_one_away(word1, word2):
#     res = 0
#     if len(word1) != len(word2):
#         return False
#     for i in range(len(word1)):
#         if word1[i] != word2[i]:
#             res += 1
#         if res == 0:
#             return False
#     if res >= 2:
#         return False
#     else:
#         return True
#
# # считываем данные
# txt1 = input()
# txt2 = input()
#
# # вызываем функцию
# print(is_one_away(txt1, txt2))


# ''' or '''
#
# # объявление функции
# def is_one_away(word1, word2):
#     mismatches = 0
#
#     if len(word1) == len(word2):
#         for i in range(len(word1)):
#             if word1[i] != word2[i]:
#                 mismatches += 1
#
#         return mismatches == 1
#
#     return False
#
#
# # считываем данные
# txt1 = input()
# txt2 = input()
#
# # вызываем функцию
# print(is_one_away(txt1, txt2))
#
#
# ''' or '''
#
# # объявление функции
# def is_one_away(word1, word2):
#     a = 0
#     for i in range(len(word1)):
#         if word1[i] != word2[i]:
#             a += 1
#     return len(word1) == len(word2) and a == 1
#
# # считываем данные
# txt1 = input()
# txt2 = input()
#
# # вызываем функцию
# print(is_one_away(txt1, txt2))


# ''' Палиндром 🌶️ '''
#
# # объявление функции
# def is_palindrome(text):
#     # Удалить символы , . ! ? - и пробелы из текста
#     cleaned_text = "".join(c.lower() for c in text if c.isalnum())
#
#     # Проверить, является ли очищенный текст палиндромом
#     return cleaned_text == cleaned_text[::-1]
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_palindrome(txt))
#
#
# ''' or '''
#
# def is_palindrome(text):
#     symbols = [' ', ',', '.', '!', '?', '-']
#     for c in symbols:
#         text = text.replace(c, '')
#     text = text.lower()
#     return text == text[::-1]
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_palindrome(txt))
#
#
# ''' or '''
#
# # объявление функции
# def is_palindrome(text):
#     text = [i.lower() for i in text if i not in (',.!?- ')]
#     return text == text[::-1]
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_palindrome(txt))




# ''' действительный пароль BEEGEEK  '''
#
#
# def is_palindrome(number):
#     # Функция для проверки, является ли число палиндромом
#     return str(number) == str(number)[::-1]
#
# def is_prime(number):
#     # Функция для проверки, является ли число простым
#     if number <= 1:
#         return False
#     for i in range(2, int(number**0.5) + 1):
#         if number % i == 0:
#             return False
#     return True
#
# def is_valid_password(password):
#     # Разбиваем пароль на a, b и c
#     parts = password.split(":")
#     if len(parts) != 3:
#         return False
#
#     a, b, c = map(int, parts)
#
#     # Проверяем условия
#     if is_palindrome(a) and is_prime(b) and c % 2 == 0:
#         return True
#     else:
#         return False
#
# # Пример использования функции
# password = input()
# result = is_valid_password(password)
# if result:
#     print("Пароль действителен")
# else:
#     print("Пароль не действителен")


# ''' or '''
#
# def is_valid_password(password):
#     password = password.split(':')
#     a, b, c = password[0], int(password[1]), int(password[2])
#     if len(password) != 3 or a != a[::-1] or c % 2 != 0:
#         return False
#     for i in range(2, b):
#         if b % i == 0:
#             return False
#     return True
#
#
# psw = input()
# print(is_valid_password(psw))


# ''' Правильная скобочная последовательность 🌶️ '''
#
# # объявление функции
# def is_correct_bracket(text):
#     stack = []  # Инициализируем стек для скобок
#
#     for char in text:
#         if char == "(":
#             stack.append(char)  # Если символ - открывающая скобка, добавляем её в стек
#         elif char == ")":
#             if not stack or stack.pop() != "(":  # Если символ - закрывающая скобка, проверяем стек
#                 return False  # Если стек пуст или верхний элемент стека не парный, последовательность неправильная
#
#     return len(stack) == 0  # Проверяем, что стек пуст после обработки всех символов
#
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_correct_bracket(txt))



# ''' or '''
#
# # объявление функции
# def is_correct_bracket(text):
#     while "()" in text:
#         text = text.replace("()", "")
#
#     return text == ""
#
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_correct_bracket(txt))



# ''' принимает в качестве аргумента строку в «верблюжьем регистре» и преобразует его в «змеиный регистр».'''
#
# def convert_to_python_case(text):
#     s = text[0].lower()
#     for i in text[1:]:
#         if i.isupper():
#             s = s + '_' + i.lower()
#         else:
#             s += i
#     return s
#
# txt = input()
# print(convert_to_python_case(txt))
#
#
# ''' or '''
#
#
# def convert_to_python_case(text):
#     s = ''
#     for el in text:
#         if el.isupper():
#             s += '_'
#         s += el.lower()
#     return s[1:]
#
#
# print(convert_to_python_case(input()))
#
#
# ''' or '''
#
#
# def convert_to_python_case(text):
#     return ''.join(['_' + i if i.isupper() else i for i in text]).lstrip('_').lower()
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(convert_to_python_case(txt))



''' Функции с возвратом нескольких значений '''


# ''' принимает в качестве аргументов координаты концов отрезка
#  и возвращает координаты точки являющейся серединой данного отрезка.'''

# # объявление функции
# def get_middle_point(x1, y1, x2, y2):
#     return (x1 + x2) / 2, (y1 + y2) / 2
#
# # считываем данные
# x_1, y_1 = int(input()), int(input())
# x_2, y_2 = int(input()), int(input())
#
# # вызываем функцию
# x, y = get_middle_point(x_1, y_1, x_2, y_2)
# print(x, y)


# ''' принимает в качестве аргумента радиус окружности и возвращает два значения:
#     длину окружности и площадь круга, ограниченного данной окружностью.'''
#
# from math import *
#
# # объявление функции
# def get_circle(radius):
#     return 2 * pi * radius, pi * radius**2
#
#
# # считываем данные
# r = float(input())
#
# # вызываем функцию
# length, square = get_circle(r)
# print(length, square)


#
# ''' Корни уравнения 🌶️🌶️ '''
#
#
# # объявление функции
# import math
#
#
# def solve(a, b, c):
#     # Вычисляем дискриминант
#     discriminant = b ** 2 - 4 * a * c
#
#     # Вычисляем корни
#     if discriminant > 0:
#         root1 = (-b + math.sqrt(discriminant)) / (2 * a)
#         root2 = (-b - math.sqrt(discriminant)) / (2 * a)
#         return min(root1, root2), max(root1, root2)
#
#     elif discriminant == 0:
#         root = -b / (2 * a)
#         return root, root
#
#
# # считываем данные
# a, b, c = int(input()), int(input()), int(input())
#
# # вызываем функцию
# x1, x2 = solve(a, b, c)
# print(x1, x2)
#
#
#
# ''' or '''
#
#
# def solve(a, b, c):
#     D = b ** 2 - 4 * a * c
#     x1 = (-b - D ** 0.5) / (2 * a)
#     x2 = (-b + D ** 0.5) / (2 * a)
#
#     return min(x1, x2), max(x1, x2)
#
#
# # считываем данные
# a, b, c = int(input()), int(input()), int(input())
#
# # вызываем функцию
# x1, x2 = solve(a, b, c)
# print(x1, x2)

