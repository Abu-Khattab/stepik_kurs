# info = {'name': 'Sam', 'age': 28, 'job': 'Teacher'}
#
# info['name'] = 'Timur'
# info['email'] = 'timur-guev@yandex.ru'
#
# print(info)


# ''' сколько именно раз встречается каждое из чисел '''
#
# numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
# def any_number(number):
#
#     result = {}
#     for num in numbers:
#         if num not in result:
#             result[num] = 1
#         else:
#             result[num] += 1
#
#     return result
#
# print(any_number(numbers))
#
#
# ''' or much easier to metod - get()'''
#
# numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
#
# result = {}
# for num in numbers:
#     result[num] = result.get(num, 0) + 1
#
# print(result)


# ''' операцию конкатенации для словарей metod update() or |= '''
#
#
# info1 = {'name': 'Bob',
#          'age': 25,
#          'job': 'Dev'}
#
# info2 = {'age': 30,
#          'city': 'New York',
#          'email': 'bob@dev.com'}
#
# info1.update(info2) #  or #  info1 |= info2
# print(info1)




# ''' setdefault() позволяет получить значение из словаря по заданному ключу,
#  автоматически добавляя элемент словаря, если он отсутствует.'''
#
#
# info = {'name': 'Bob',
#         'age': 25}
#
# name1 = info.setdefault('name')           # параметр default не задан
# name2 = info.setdefault('name', 'Max')    # параметр default задан
#
# print(name1)
# print(name2)
#
#
# ''' Если ключ key отсутствует в словаре, то метод вставляет переданное значение default'''
#
# info = {'name': 'Bob',
#         'age': 25}
#
# job = info.setdefault('job', 'Dev')
# print(info)
# print(job)


# ''' если значение default не передано в метод, то вставится значение None'''
#
# info = {'name': 'Bob',
#         'age': 25}
#
# job = info.setdefault('job')
# print(info)
# print(job)



# ''' работа метода copy() '''
#
# info = {'name': 'Bob',
#         'age': 25,
#         'job': 'Dev'}
#
# new_info = info
# new_info['name'] = 'Tim'
#
# print(info)
# print(new_info)
#
#
# '''  copy() '''
#
#
# info = {'name': 'Bob',
#         'age': 25,
#         'job': 'Dev'}
#
# new_info = info.copy()
# new_info['name'] = 'Tim'
#
# print(info)
# print(new_info)


# ''' Словарь можно использовать вместо нескольких вложенных условий '''
#
#
# num = int(input())
#
# if num == 1:
#     description = 'One'
# elif num == 2:
#     description = 'Two'
# elif num == 3:
#     description = 'Three'
# else:
#     description = 'Unknown'
#
# print(description)
#
#
# ''' вместо нескольких вложенных условий '''
#
# num = int(input())
#
# description = {1: 'One', 2: 'Two', 3: 'Three'}
#
# print(description.get(num, 'Unknown'))



# ''' генерируется словарь с ключём значением '''
#
# print({i: chr(65+i) for i in range(11)})
#
#
# result = {i: i ** 2 for i in range(1, 16)}
# print(result)
#
#
# result = dict(zip(range(1, 16), [i * i for i in range(1, 16)])) # zip()
#
#
#
# result = {}
# for i in range(1, 16):
#     result.setdefault(i, i**2)  # setdefault()
#
#     result = {}
#
#
#
# for i in range(1, 16):
#     result[i] = i ** 2  # циклом
#
#
#
# result = {}
# for i in range(1, 16):
#     result[i] = result.get(i, i**2)  # get()
#
#
#
# result = {key : key ** 2 for key in range(1, 16)}  # генератор



# ''' ля каждого символа строки text будет подсчитано количество его вхождений. '''
#
# text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
#
# result = {}
#
# for i in text:
#     result[i] = result.get(i, 0) + 1
#
# print(result)


# ''' or '''
#
# text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
#
# result = {elem: text.count(elem) for elem in set(text)}
# print(result)
#
# ''' or '''
#
# text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
# result = {elem: text.count(elem) for elem in text}
# print(result)



# dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
# dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
#
# result = {}
#
# # Объединяем словари, складывая значения с одинаковыми ключами
# for item in dict1.keys():
#     if item in dict2:
#         result[item] = dict1[item] + dict2[item]
#     else:
#         result[item] = dict1[item]  # Используйте result[item], а не result = dict1[item]
#
# # Добавляем ключи из dict2, которых нет в result
# for item in dict2.keys():
#     if item not in result:
#         result[item] = dict2[item]
#
# print(result)



#
#
# s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
#
# # Разбиваем строку на слова
# words = s.split()
#
# # Создаем словарь для подсчета частоты каждого слова
# word_count = {}
#
# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
#
# # Находим наиболее часто встречающееся слово
# max_count = max(word_count.values())
# most_frequent_words = [word for word, count in word_count.items() if count == max_count]
#
# # Если есть несколько наиболее часто встречающихся слов, выбираем то, которое меньше в лексикографическом порядке
# most_frequent_words.sort()
# print(most_frequent_words[0])
#
#
#
# ''' or '''
#
# s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
#
# d = {}
# for w in s.split():
#     d[w] = d.get(w, 0) + 1
# print(min(d, key=lambda x: (-d[x], x)))
#
#
# ''' or '''
#
# s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
# result = {l: s.split().count(l) for l in set(s.split())}
#
# print(min(l for l in result if result[l]==max(result.values())))



# ''' для каждого владельца будут перечислены его собаки '''

# pets = [('Hatiko', 'Parker', 'Wilson', 50),
#         ('Rusty', 'Josh', 'King', 25),
#         ('Fido', 'John', 'Smith', 28),
#         ('Butch', 'Jake', 'Smirnoff', 18),
#         ('Odi', 'Emma', 'Wright', 18),
#         ('Balto', 'Josh', 'King', 25),
#         ('Barry', 'Josh', 'King', 25),
#         ('Snape', 'Hannah', 'Taylor', 40),
#         ('Horry', 'Martha', 'Robinson', 73),
#         ('Giro', 'Alex', 'Martinez', 65),
#         ('Zooma', 'Simon', 'Nevel', 32),
#         ('Lassie', 'Josh', 'King', 25),
#         ('Chase', 'Martha', 'Robinson', 73),
#         ('Ace', 'Martha', 'Williams', 38),
#         ('Rocky', 'Simon', 'Nevel', 32)]
#
# result = {}
#
# for pet in pets:
#     owner = pet[1:]
#     if owner in result:
#         result[owner].append(pet[0])
#     else:
#         result[owner] = [pet[0]]
#
# print(result)



# ''' or '''
#
# pets = [('Hatiko', 'Parker', 'Wilson', 50),
#         ('Rusty', 'Josh', 'King', 25),
#         ('Fido', 'John', 'Smith', 28),
#         ('Butch', 'Jake', 'Smirnoff', 18),
#         ('Odi', 'Emma', 'Wright', 18),
#         ('Balto', 'Josh', 'King', 25),
#         ('Barry', 'Josh', 'King', 25),
#         ('Snape', 'Hannah', 'Taylor', 40),
#         ('Horry', 'Martha', 'Robinson', 73),
#         ('Giro', 'Alex', 'Martinez', 65),
#         ('Zooma', 'Simon', 'Nevel', 32),
#         ('Lassie', 'Josh', 'King', 25),
#         ('Chase', 'Martha', 'Robinson', 73),
#         ('Ace', 'Martha', 'Williams', 38),
#         ('Rocky', 'Simon', 'Nevel', 32)]
#
# result = {}
# for pet in pets:
#     result.setdefault(pet[1:], []).append(pet[0])
#
# print(result)
#
#
# ''' or '''
#
# pets = [('Hatiko', 'Parker', 'Wilson', 50),
#         ('Rusty', 'Josh', 'King', 25),
#         ('Fido', 'John', 'Smith', 28),
#         ('Butch', 'Jake', 'Smirnoff', 18),
#         ('Odi', 'Emma', 'Wright', 18),
#         ('Balto', 'Josh', 'King', 25),
#         ('Barry', 'Josh', 'King', 25),
#         ('Snape', 'Hannah', 'Taylor', 40),
#         ('Horry', 'Martha', 'Robinson', 73),
#         ('Giro', 'Alex', 'Martinez', 65),
#         ('Zooma', 'Simon', 'Nevel', 32),
#         ('Lassie', 'Josh', 'King', 25),
#         ('Chase', 'Martha', 'Robinson', 73),
#         ('Ace', 'Martha', 'Williams', 38),
#         ('Rocky', 'Simon', 'Nevel', 32)]
# result = {}
# for i in pets:
#     key = i[1:]
#     if key not in result:
#         result[key] = [i[0]]
#     else:
#         result[key].append(i[0])
#
#
#
# ''' or '''
#
# pets = [('Hatiko', 'Parker', 'Wilson', 50),
#         ('Rusty', 'Josh', 'King', 25),
#         ('Fido', 'John', 'Smith', 28),
#         ('Butch', 'Jake', 'Smirnoff', 18),
#         ('Odi', 'Emma', 'Wright', 18),
#         ('Balto', 'Josh', 'King', 25),
#         ('Barry', 'Josh', 'King', 25),
#         ('Snape', 'Hannah', 'Taylor', 40),
#         ('Horry', 'Martha', 'Robinson', 73),
#         ('Giro', 'Alex', 'Martinez', 65),
#         ('Zooma', 'Simon', 'Nevel', 32),
#         ('Lassie', 'Josh', 'King', 25),
#         ('Chase', 'Martha', 'Robinson', 73),
#         ('Ace', 'Martha', 'Williams', 38),
#         ('Rocky', 'Simon', 'Nevel', 32)]
#
# result = {}
# for i in pets:
#     result[i[1:]] = result.get(i[1:], []) + i[0].split()


# ''' Самое редкое слово 🌶️ '''
#
# lst = [word.strip('.,!?:;-') for word in input().lower().split()]
#
# result = {elem: lst.count(elem) for elem in set(lst)}
#
# min_value = min(result.values())
# min_keys = [key for key in result if result[key] == min_value]
# min_key = min(min_keys)
# print(f"Ключ с минимальным значением (лексикографически первый): {min_key}, Значение: {min_value}")
#
#
#
# ''' or '''
#
# st = [i.strip('.,!?:;-') for i in input().lower().split()]
# print(min(st, key=lambda x: (st.count(x), x)))
#
#
# ''' or '''
#
# words = [word.lower().strip('.,;:-?!  ') for word in input().split()]
# result = {}
#
# for word in words:
#     result[word] = result.get(word, 0) +1
# print(min(word for word in words if result[word] == min(result.values())))


# ''' Исправление дубликатов 🌶️ '''
# ''' or - ИИ '''

# words = [word.lower() for word in input().split()]
# result = {}
# count = {}
# output = []
#
# for word in words:
#     count[word] = count.get(word, 0) + 1
#     if count[word] > 1:
#         result[word] = f"{word}_{count[word] - 1}"
#     else:
#         result[word] = word
#     output.append(result[word])
#
# output_text = " ".join(output)
# print(output_text)



# ''' or - ИИ '''

# text = input().split()
# identifier_count = {}
# result = []
#
# for identifier in text:
#     if identifier not in identifier_count:
#         identifier_count[identifier] = 1
#         result.append(identifier)
#     else:
#         identifier_count[identifier] += 1
#         result.append(f"{identifier}_{identifier_count[identifier]}")
#
# print(" ".join(result))
