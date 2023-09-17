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



