# fruits = ["apples", "bananas", "strawberry"]
# new_fruit = []
# for fruit in fruits:
#     fruit = fruit.upper()
#     new_fruit.append(fruit)
#
#
# print(new_fruit)
#
#
# ''' or '''
#
# fruit_components = [fruit.upper() for fruit in fruits]
#
# print(fruit_components)


# ''' Ключом будет позиция числа в списке numbers, а значением – его квадрат. '''
#
# # numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]
# #
# # result = {i: numbers[i] ** 2 for i in range(len(numbers))}
# # print(result)



# ''' словарь result, состоящий из всех элементов словаря colors, кроме тех,
#     у которых значением является None.'''
#
# colors = {'c1': 'Red', 'c2': 'Grey', 'c3': None,
#           'c4': 'Green', 'c5': 'Yellow', 'c6': 'Pink', 'c7': 'Orange', 'c8': None,
#           'c9': 'White', 'c10': 'Black', 'c11': 'Violet', 'c12': 'Gold', 'c13': None,
#           'c14': 'Amber', 'c15': 'Azure', 'c16': 'Beige', 'c17': 'Bronze', 'c18': None,
#           'c19': 'Lilac', 'c20': 'Pearl', 'c21': None,
#           'c22': 'Sand', 'c23': None}
#
# result = {i: colors[i] for i in colors if colors[i] is not None}

# or
# result = {x: colors[x] for x in colors if colors[x]}
#
# print(result)



# ''' словарь result, состоящий из всех элементов словаря favorite_numbers ,
#     значения которых являются двузначными числами.'''
#
# favorite_numbers = {'timur': 17, 'ruslan': 7, 'larisa': 19, 'roman': 123, 'rebecca': 293, 'ronald': 76, 'dorothy': 62,
#                     'harold': 36, 'matt': 314, 'kim': 451, 'rosaly': 18, 'rustam': 89, 'soltan': 111, 'amir': 654,
#                     'dima': 390, 'amiran': 777, 'geor': 999, 'sveta': 75, 'rita': 909, 'kirill': 404, 'olga': 271,
#                     'anna': 55, 'madlen': 876}
#
# result = {key: value for key, value in favorite_numbers.items() if 9 < value <= 99}
#
# # or # result = {k : v for k, v in f.items() if len(str(v)) == 2}
# print(result)



# ''' словарь months , в которых ключ и значение поменялись местами. '''
#
# months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
# 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
#
##or
## result = {months[i]: i for i in months}
#
#
# result = {value: key for key, value in months.items()}
# print(result)



# ''' Словарь result, в котором числа будут ключами, а слова – значениями. '''
#
# s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
#
# result = {int(i.split(':')[0]): i.split(':')[1] for i in s.split()}
#
# # ''' or # result = {int(k):v for k, v in [l.split(':') for l in s.split()]}'''
#
# print(result)



# ''' значением – отсортированный по возрастанию список всех его делителей начиная с 1 '''
#
# numbers = [1, 6, 18]
#
# result = {key: [i for i in range(1, key + 1) if key % i == 0] for key in numbers}
# print(result)



# ''' Список соответствующих кодов ASCII символов данной строки. '''
#
# words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']
#
# result = {key: [ord(i) for i in key] for key in words}
# print(result)




# """ За исключением тех, ключи которых есть в списке remove_keys """
#
# letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N',
#            14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 26: 'Z'}
#
# remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]
#
# result = {key: value for key, value in letters.items() if key not in remove_keys}
# print(result)


# ''' всех элементов словаря students , где указан рост больше 167 см, а вес меньше 75 кг.'''

# students = {'Timur': (170, 75), 'Ruslan': (180, 105), 'Sultan': (192, 68), 'Roman': (175, 70), 'Madlen': (160, 50),
#             'Stefani': (165, 70), 'Tom': (190, 90), 'Jerry': (180, 87), 'Anna': (172, 67), 'Scott': (168, 78),
#             'John': (186, 79), 'Alex': (195, 120), 'Max': (200, 110), 'Barak': (180, 89), 'Donald': (170, 80),
#             'Rustam': (186, 100), 'Alice': (159, 59), 'Rita': (170, 80), 'Mary': (175, 69), 'Jane': (190, 80)}
#
# result = {key: value for key, value in students.items() if value[0] > 167 and value[1] < 75}
# print(result)



# ''' Первый элемент каждого кортежа, а значением – кортеж из оставшихся двух элементов '''
#
# tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 21), (22, 23, 24),
#           (25, 26, 27), (28, 29, 30), (31, 32, 33), (34, 35, 36)]
#
# result = {key[0]: key[1:] for key in tuples}
# print(result)



# ''' получить список result, содержащий вложенные словари '''
#
# student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013']
# student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti',
#                  'Khalid Hussain', 'Ethan Hawk', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy']
# student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]
#
# result = [{key: {name: numer}} for key, name, numer in zip(student_ids, student_names, student_grades)]
# ''' or # result =  [{student_ids[i]:{student_names[i]:student_grades[i]}} for i in range (len(student_ids))] '''
# print(result)



# ''' Как "перевернуть" словарь '''
#
# dicts = {1: 'a', 2: 'b', 3: 'a', 4: 'a'}
# new_dicts = {v: k for k, v in dicts.items()}
# print(new_dicts)
