# ''' Анаграммы 1 '''
#
# from collections import Counter
#
# a, b = input(), input()
#
# # Создаем счетчики символов для обеих строк
# counter_a = Counter(a)
# counter_b = Counter(b)
#
# # Сравниваем счетчики символов
# if counter_a == counter_b:
#     print("YES")
# else:
#     print("NO")


# ''' or '''
#
# print('YES' if sorted(input()) == sorted(input()) else 'NO')


# '''or '''
#
# a = input()
# b = input()
# c = {k: a.count(k) for k in a}
# d = {k: b.count(k) for k in b}
# print (('NO', 'YES')[c==d])


# ''' Анаграммы 2 '''
#
# from collections import Counter
#
# a, b = input().lower(), input().lower()
#
# a = ''.join(char for char in a if char.isalpha()).split()
# b = ''.join(char for char in b if char.isalpha()).split()
#
# # Сортируем символы в строках
# a = ''.join(sorted(a))
# b = ''.join(sorted(b))
#
# # Создаем счетчики символов для обеих строк
# counter_a = Counter(a)
# counter_b = Counter(b)
#
# # Сравниваем счетчики символов
# if counter_a == counter_b:
#     print("YES")
# else:
#     print("NO")
#
#
# ''' or '''
#
# def s(word):
#     res = {}
#     for i in word.lower():
#         if i.isalpha():
#             res[i] = res.get(i, 0) + 1
#     return res
#
#
# print(("NO", "YES")[s(input()) == s(input())])
#
#
#
# ''' or '''
#
# s1 = [i for i in input().lower() if i.isalpha()]
# s2 = [i for i in input().lower() if i.isalpha()]
#
# print('YES' if sorted(s1) == sorted(s2) else 'NO')
#
#
# ''' or '''
#
# a, b = [sorted([i for i in input().lower() if i.isalpha()]) for _ in "ab"]
# print(["NO", "YES"][a == b])
#
#
# ''' or '''
#
# w1, w2 = input().lower(), input().lower()
# dc1 = {i: w1.count(i) for i in set(w1) if i not in ':,!.;-? '}
# dc2 = {i: w2.count(i) for i in set(w2) if i not in ':,!.;-? '}
# print('YES' if dc1 == dc2 else 'NO')


# ''' Словарь синонимов '''
#
# mydict = {}
# mydict_r = {}
#
# for _ in range(int(input())):
#     key, value = input().split()
#     mydict[key] = value
#     mydict_r[value] = key
#
# key = input()
#
# if mydict.get(key):
#     print(mydict[key])
# if mydict_r.get(key):
#     print(mydict_r[key])
#
#
#
# ''' or '''
#
# mydict = {}
# mydict_r = {}
#
# for _ in range(int(input())):
#     key, value = input().split()
#     mydict[key] = value
#     mydict_r[value] = key
#
# input_key = input()
# if input_key in mydict:
#     result = mydict[input_key]
#     print(result)
# elif input_key in mydict_r:
#     result = mydict_r[input_key]
#     print(result)
# else:
#     print("Не найдено")
#
# ''' or '''
#
# words = {}
# for _ in range(int(input())):
#     a, b = input().split()
#     words[a], words[b] = b, a
# print(words[input()])
#
#
# ''' or '''
#
# d = dict((input().split() for i in range(int(input()))))
# ad = {v: k for k, v in d.items()}
# key = input()
# print(ad.get(key, d.get(key)))
#
#
# ''' or '''
#
# print({w[i]: w[not i] for _ in range(int(input())) for w in [input().split()] for i in (0, 1)}[input()])


#
# ''' Словарь программиста '''
#
#
# # Ввод количества слов в словаре
# n = int(input())
#
# # Создание пустого словаря
# dictionary = {}
#
# # Заполнение словаря словами и их определениями
# for _ in range(n):
#     word, definition = input().split(": ")
#     dictionary[word.lower()] = definition
#
# # Ввод количества поисковых слов
# m = int(input())
#
# # Поиск определений
# for _ in range(m):
#     search_word = input().lower()
#     if search_word in dictionary:
#         print(dictionary[search_word])
#     else:
#         print("Не найдено")
#
#
#
# ''' or '''
#
# mydict = {}
#
# for _ in range(int(input())):
#     key, value = input().split(': ')
#     mydict[key.lower()] = value
#
# for _ in range(int(input())):
#     print(mydict.get(input().lower(), 'Не найдено'))


# ''' Страны и города '''
#
# # Создаем пустой словарь для хранения информации о странах и городах
# countries = {}
#
# # Считываем количество стран
# n = int(input())
#
# # Считываем информацию о странах и городах
# for _ in range(n):
#     line = input().split()
#     country = line[0]
#     cities = line[1:]
#     countries[country] = cities
#
# # Создаем словарь для быстрого поиска страны по названию города
# city_to_country = {}
# for country, cities in countries.items():
#     for city in cities:
#         city_to_country[city] = country
#
# # Считываем количество запросов
# m = int(input())
#
# # Обрабатываем запросы по городам
# for _ in range(m):
#     city = input()
#     if city in city_to_country:
#         country = city_to_country[city]
#         print(country)
#     else:
#         print("Не найдено")
#
#
#
# ''' or '''
#
# d = {}
# for _ in range(int(input())):
#     country, *cities = input().split()
#     d.update(dict.fromkeys(cities, country))
# for _ in range(int(input())):
#     print(d[input()])
#
#
#
#
# ''' or '''
#
# d = {}
# for i in range(int(input())):
#     l = input().split()
#     d[l[0]] = l[1:]
#
# for i in range(int(input())):
#     k = input()
#     for key, value in d.items():
#         if k in value:
#             print(key)




# ''' Телефонная книга '''
#
# # создание пустого словаря
# phone_book = {}
#
# # Ввод количества номеров телефонов
# for _ in range(int(input())):
#     phone, name = input().lower().split()
#     if name in phone_book:
#         phone_book[name].append(phone)
#     else:
#         phone_book[name] = [phone]
#
#
# # Ввод количества запросов
# # Обработка запросов
#
# for _ in range(int(input())):
#     k = input().lower()
#     if k in phone_book:
#         print(*phone_book[k])
#     else:
#         print("абонент не найден")
#
#
#
# ''' or '''
#
# dct = {}
# for _ in range(int(input())):
#     phone, name = input().lower().split()
#     dct.setdefault(name, []).append(phone)
# for _ in range(int(input())):
#     print(*dct.get(input().lower(), ['абонент не найден']))



# ''' Секретное слово '''
#
# s = input()
#
# my_dict = {}
#
# for _ in range(int(input())):
#     value, key = input().split(': ')
#     my_dict[int(key)] = value
#
# for symbol in s:
#     print(my_dict[s.count(symbol)], end='')


