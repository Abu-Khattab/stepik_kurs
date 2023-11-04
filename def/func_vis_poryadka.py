# ''' Функция map() '''
#
# def f(x):
#     return x**2     # тело функции, которая преобразует аргумент x
#
#
# old_list = [1, 2, 4, 9, 10, 25]
# new_list = []
# for item in old_list:
#     new_item = f(item)
#     new_list.append(new_item)
#
# print(old_list)
# print(new_list)
#
#
# """ or """
#
# def map(function, items):
#     result = []
#     for item in items:
#         new_item = function(item)
#         result.append(new_item)
#     return result
#
#
# def square(x):
#     return x**2
#
#
# def cube(x):
#     return x**3
#
#
# numbers = [1, 2, -3, 4, -5, 6, -9, 0]
#
# strings = list(map(str, numbers))        # используем в качестве преобразователя - функцию str
# abs_numbers = list(map(abs, numbers))    # используем в качестве преобразователя - функцию abs
#
# squares = list(map(square, numbers))     # используем в качестве преобразователя - функцию square
# cubes = list(map(cube, numbers))         # используем в качестве преобразователя - функцию cube
#
# print(strings)
# print(abs_numbers)
# print(squares)
# print(cubes)


# ''' Функция filter '''
#
#
# def is_odd(num):
#     return num % 2
#
#
# def is_word_long(word):
#     return len(word) > 6
#
#
# numbers = list(range(15))
# words = ['В', 'новом', 'списке', 'останутся', 'только', 'длинные', 'слова']
#
# odd_numbers = list(filter(is_odd, numbers))
# large_words = list(filter(is_word_long, words))
#
# print(odd_numbers)
# print(large_words)


# ''' Функция reduce '''
#
#
# def reduce(operation, items, initial_value):
#     acc = initial_value
#     for item in items:
#         acc = operation(acc, item)
#
#     return acc
#
#
# def add(x, y):
#     return x+y
#
#
# def mult(x, y):
#     return x*y
#
#
# numbers = [1, 2, 3, 4, 5]
#
# total = reduce(add, numbers, 0)
# product = reduce(mult, numbers, 1)
#
# print(total)
# print(product)


# '''  Округляет все элементы списка numbers до 2 десятичных знаков '''
#
# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def around(x):
#     return round(x, 2)
#
#
# numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013,
#            23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]
#
#
# my_list = map(around, numbers)
# for i in my_list:
#     print(i)
#
#
# ''' or '''
#
#
# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def round_two(a):
#     return round(a, 2)
#
#
# numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828,
#            1.41546]
#
# print(*map(round_two, numbers), sep='\n')




# ''' с помощью функций filter() и map() отбирает  '''
#
#
# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
#
# numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434, 1462,
#            815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289, 1155,
#            230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013, 898, 669,
#            105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336, 1268, 351,
#            1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]
#
#
# def length(x):
#     return 99 < x <= 999 and x % 5 == 2
#
#
# def cube_ostatka(x):
#     return x ** 3
#
#
# print(*map(cube_ostatka, filter(length, numbers)), sep='\n')



# ''' вычисления и вывода суммы квадратов элементов списка numbers '''
#
# def reduce(operation, items, initial_value):
#     acc = initial_value
#     for item in items:
#         acc = operation(acc, item)
#     return acc
#
#
# numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51,
#            90, 56, 65, 90, 23, 35, 11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60, 72,
#            43, 4, -6, -5, 51, 58, 60, 30, 38, 67, 62, 36, 72, 34, 82, 62, -1, 60, 82, 87, 81,
#            -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64, 38, 72, 29, 84, 38, 35, 7, 54, 31,
#            95, 78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]
#
#
# def kwadrat(x):
#     return x ** 2
#
#
# def sum_kwadrat(x, y):
#     return x + y**2
#
#
# print(reduce(sum_kwadrat, numbers, 0))
# print(sum(map(kwadrat, numbers)))


# ''' для вычисления и вывода суммы квадратов двузначных чисел, которые делятся на 7 без остатка.'''
#
# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
#
# def xx(item):
#     return item ** 2
#
#
# def fil(item):
#     return 9 < abs(item) < 100 and not item % 7
#
#
# numbers = [77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61, 298, 280, 214, 156, 227, 228, 51, -4, 202, 58, 99, 270, 219, 94, 253, 53, 235, 9, 158, 49, 183, 166, 205, 183, 266, 180, 6, 279, 200, 208, 231, 178, 201, 260, -35, 152, 115, 79, 284, 181, 92, 286, 98, 271, 259, 258, 196, -8, 43, 2, 128, 143, 43, 297, 229, 60, 254, -9, 5, 187, 220, -8, 111, 285, 5, 263, 187, 192, -9, 268, -9, 23, 71, 135, 7, -161, 65, 135, 29, 148, 242, 33, 35, 211, 5, 161, 46, 159, 23, 169, 23, 172, 184, -7, 228, 129, 274, 73, 197, 272, 54, 278, 26, 280, 13, 171, 2, 79, -2, 183, 10, 236, 276, 4, 29, -10, 41, 269, 94, 279, 129, 39, 92, -63, 263, 219, 57, 18, 236, 291, 234, 10, 250, 0, 64, 172, 216, 30, 15, 229, 205, 123, -105]
#
#
# print(sum(map(xx, filter(fil, numbers))))
#
#
#
# ''' or '''
# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
# def is_2(x):
#     return len(str(abs(x))) == 2 and x % 7 == 0
#
# def square_x(x):
#     return x*x
#
# numbers = [77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61, 298, 280, 214, 156, 227, 228, 51, -4, 202, 58, 99, 270, 219, 94, 253, 53, 235, 9, 158, 49, 183, 166, 205, 183, 266, 180, 6, 279, 200, 208, 231, 178, 201, 260, -35, 152, 115, 79, 284, 181, 92, 286, 98, 271, 259, 258, 196, -8, 43, 2, 128, 143, 43, 297, 229, 60, 254, -9, 5, 187, 220, -8, 111, 285, 5, 263, 187, 192, -9, 268, -9, 23, 71, 135, 7, -161, 65, 135, 29, 148, 242, 33, 35, 211, 5, 161, 46, 159, 23, 169, 23, 172, 184, -7, 228, 129, 274, 73, 197, 272, 54, 278, 26, 280, 13, 171, 2, 79, -2, 183, 10, 236, 276, 4, 29, -10, 41, 269, 94, 279, 129, 39, 92, -63, 263, 219, 57, 18, 236, 291, 234, 10, 250, 0, 64, 172, 216, 30, 15, 229, 205, 123, -105]
#
# print(sum(map(square_x, filter(is_2, numbers))))


# ''' принимающую на вход функцию и список значений и возвращающую список, в котором каждое значение будет результатом
#     применения переданной функции к переданному списку.'''
#
# def func_apply(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def add3(x):
#     return x + 3
#
#
# def mul7(x):
#     return x * 7
#
#
# print(func_apply(mul7, [1, 2, 3, 4, 5, 6]))
# print(func_apply(add3, [1, 2, 3, 4, 5, 6]))
# print(func_apply(str, [1, 2, 3, 4, 5, 6]))


# ''' преобразует список floats в список чисел, возведенных в квадрат и округленных с точностью до одного десятичного знака;
#     фильтрует список words и оставляет только палиндромы длиной более 4 символов;
#     находит произведение чисел из списка numbers. '''
#
#
# from functools import reduce
#
#
# floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
# words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
# numbers = [4, 6, 9, 23, 5]
#
# # Исправьте этот код
# map_result = list(map(lambda num: round(num ** 2, 1), floats))
# filter_result = list(filter(lambda name: len(name) > 4 and name[::-1] == name, words))
# reduce_result = reduce(lambda num1, num2: num1 * num2, numbers, 1)
#
# print(map_result)
# print(filter_result)
# print(reduce_result)



# data = [['Tokyo', 35676000, 'primary'],
#         ['New York', 19354922, 'nan'],
#         ['Mexico City', 19028000, 'primary'],
#         ['Mumbai', 18978000, 'admin'],
#         ['Sao Paulo', 18845000, 'admin'],
#         ['Delhi', 15926000, 'admin'],
#         ['Shanghai', 14987000, 'admin'],
#         ['Kolkata', 14787000, 'admin'],
#         ['Los Angeles', 12815475, 'nan'],
#         ['Dhaka', 12797394, 'primary'],
#         ['Buenos Aires', 12795000, 'primary'],
#         ['Karachi', 12130000, 'admin'],
#         ['Cairo', 11893000, 'primary'],
#         ['Rio de Janeiro', 11748000, 'admin'],
#         ['Osaka', 11294000, 'admin'],
#         ['Beijing', 11106000, 'primary'],
#         ['Manila', 11100000, 'primary'],
#         ['Moscow', 10452000, 'primary'],
#         ['Istanbul', 10061000, 'admin'],
#         ['Paris', 9904000, 'primary']]
#
#
# results = 'Cities: ' + ', '.join(sorted([city[0] for city in data if city[1]>10**7 and city[2]== 'primary']))
# print(results)


# ''' or '''
#
#
# from functools import reduce
#
# data=[['Tokyo', 35676000, 'primary'],
#       ['New York', 19354922, 'nan'],
#       ['Mexico City', 19028000, 'primary'],
#       ['Mumbai', 18978000, 'admin'],
#       ['Sao Paulo', 18845000, 'admin'],
#       ['Delhi', 15926000, 'admin'],
#       ['Shanghai', 14987000, 'admin'],
#       ['Kolkata', 14787000, 'admin'],
#       ['Los Angeles', 12815475, 'nan'],
#       ['Dhaka', 12797394, 'primary'],
#       ['Buenos Aires', 12795000, 'primary'],
#       ['Karachi', 12130000, 'admin'],
#       ['Cairo', 11893000, 'primary'],
#       ['Rio de Janeiro', 11748000, 'admin'],
#       ['Osaka', 11294000, 'admin'],
#       ['Beijing', 11106000, 'primary'],
#       ['Manila', 11100000, 'primary'],
#       ['Moscow', 10452000, 'primary'],
#       ['Istanbul', 10061000, 'admin'],
#       ['Paris', 9904000, 'primary']]
#
# cities = filter(lambda city: city[1] > 10 ** 7 and city[2] == 'primary', data)
# cities = map(lambda city: city[0], cities)
# cities = sorted(cities)
# cities = 'Cities: ' + reduce(lambda city1, city2: f'{city1}, {city2}', cities)


# ''' lambda function '''
#
# func = lambda x: x % 19 == 0 or x % 13 == 0
# func = lambda x: x.lower().startswith('a') and x.lower().endswith('a')
# func = lambda x: x[0].lower() == x[-1].lower() == 'a'
# func = lambda x: (x[0] + x[-1]).lower() == 'aa'
# func=lambda x: x[0] in 'aA' and x[-1] in 'aA'


# is_non_negative_num = lambda x: x.replace('.', '').isdigit() and x.count('.') < 2


# is_num = lambda x: '-' not in x[1:] and x.replace('-', '', 1).replace('.', '', 1).isdigit()


# words = ['beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish', 'abuse', 'abuse', 'bid',
#          'wednesday', 'able', 'betray', 'accident', 'abduct', 'bigot', 'bet', 'abandon',
#          'besides', 'access', 'friday', 'bestow', 'abound', 'absent', 'beware', 'abundant',
#          'abnormal', 'aboard', 'about', 'accelerate', 'abort', 'thursday', 'tuesday', 'sunday',
#          'berth', 'beyond', 'benevolent', 'abate', 'abide', 'bicycle', 'beside', 'accept',
#          'berry', 'bewilder', 'abrupt', 'saturday', 'accessory', 'absorb']
#
#
# result = sorted(list(filter(lambda x: len(x) == 6, words)))
# print(*result)



# numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81,
#            66, 83, 41, 80, 80, 93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21,
#            72, 32, 41, 59, 35, 64, 49, 78, 83, 27, 57, 53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56,
#            80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66, 29, 88, 94, 37, 44, 2, 38, 36,
#            32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]
#
#
#
# f = list(map(lambda x: x // 2 if x % 2 == 0 else x, filter(lambda x: x <= 47 or x % 2 == 0, numbers)))
#
# print(*f)


# numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81,
#            66, 83, 41, 80, 80, 93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21,
#            72, 32, 41, 59, 35, 64, 49, 78, 83, 27, 57, 53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56,
#            80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66, 29, 88, 94, 37, 44, 2, 38, 36,
#            32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]
#
#
#
# f = list(map(lambda x: x // 2 if x % 2 == 0 else x, filter(lambda x: x <= 47 or x % 2 == 0, numbers)))
# a = filter(lambda x: x <= 47 or x % 2 == 0, numbers)
#
# print(*f)
# print(*a)


# data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'),
#         (1805832, 'West Virginia'), (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'),
#         (10077331, 'Michigan'), (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'),
#         (7029917, 'Massachusetts'), (6910840, 'Tennessee')]
#
#
# sorted_data = sorted(data, key=lambda state: state[1][-1], reverse=True)
# print(*list(map(lambda x: f'{x[1]}: {x[0]}', sorted_data)), sep='\n')



# '''or '''
#
# data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'), (1805832, 'West Virginia'), (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'), (10077331, 'Michigan'), (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'), (7029917, 'Massachusetts'), (6910840, 'Tennessee')]
#
# for pop, city in sorted(data, key=lambda x: x[1][-1], reverse=True):
#     print(f'{city}: {pop}')


# data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо',
#         'друг', 'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила',
#         'конец', 'вид', 'система', 'часть', 'город', 'отношение', 'женщина', 'деньги']
#
# result = list(sorted(data, key=lambda x: (len(x), x)))
# print(*result, sep='\n')
#
#
# ''' or '''
#
# data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо',
#         'друг', 'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила',
#         'конец', 'вид', 'система', 'часть', 'город', 'отношение', 'женщина', 'деньги']
#
# print(*sorted(sorted(data), key=len))



# mixed_list = ['tuesday', 'abroad', 'abuse', 'beside', 'monday', 'abate', 'accessory', 'absorb', 1384878,
#               'sunday', 'about', 454805, 'saturday', 'abort', 2121919, 2552839, 977970, 1772933, 1564063,
#               'abduct', 901271, 2680434, 'bicycle', 'accelerate', 1109147, 942908, 'berry', 433507, 'bias',
#               'bestow', 1875665, 'besides', 'bewilder', 1586517, 375290, 1503450, 2713047, 'abnormal', 2286106,
#               242192, 701049, 2866491, 'benevolent', 'bigot', 'abuse', 'abrupt', 343772, 'able', 2135748,
#               690280, 686008, 'beyond', 2415643, 'aboard', 'bet', 859105, 'accident', 2223166, 894187, 146564,
#               1251748, 2851543, 1619426, 2263113, 1618068, 'berth', 'abolish', 'beware', 2618492, 1555062,
#               'access', 'absent', 'abundant', 2950603, 'betray', 'beverage', 'abide', 'abandon', 2284251,
#               'wednesday', 2709698, 'thursday', 810387, 'friday', 2576799, 2213552, 1599022, 'accept', 'abuse',
#               'abound', 1352953, 'bid', 1805326, 1499197, 2241159, 605320, 2347441]
#
# max_number = max(filter(lambda x: isinstance(x, int), mixed_list))
# print(max_number)
#
# ''' or '''
# print(max(filter(lambda x: type(x) == int, mixed_list)))



# mixed_list = ['beside', 48, 'accelerate', 28, 'beware', 'absorb', 'besides', 'berry', 15, 65, 'abate',
#               'thursday', 76, 70, 94, 35, 36, 'berth', 41, 'abnormal', 'bicycle', 'bid', 'sunday', 'saturday',
#               87, 'bigot', 41, 'abort', 13, 60, 'friday', 26, 13, 'accident', 'access', 40, 26, 20, 75, 13, 40,
#               67, 12, 'abuse', 78, 10, 80, 'accessory', 20, 'bewilder', 'benevolent', 'bet', 64, 38, 65, 51,
#               95, 'abduct', 37, 98, 99, 14, 'abandon', 'accept', 46, 'abide', 'beyond', 19, 'about', 76, 26,
#               'abound', 12, 95, 'wednesday', 'abundant', 'abrupt', 'aboard', 50, 89, 'tuesday', 66, 'bestow',
#               'absent', 76, 46, 'betray', 47, 'able', 11]
#
# # Отфильтруем числовые и строковые элементы
# x_numbers = sorted(filter(lambda x: isinstance(x, int), mixed_list))
# x_strings = sorted(filter(lambda x: isinstance(x, str), mixed_list))
#
# # Объединим отсортированные списки
# result = x_numbers + x_strings
# print(*result)


# ''' or '''
#
# print(*sorted(mixed_list, key=lambda x: (isinstance(x, str), x)))

# ''' or '''
#
# print(*sorted(mixed_list, key=lambda x: str(x)))




# print(*map(lambda x: 255 - int(x), input().split()))

#
# from functools import reduce
#
# evaluate = lambda coeff, x: reduce(lambda s, a: s * x + a, coeff)
# print(evaluate(map(int, input().split()), int(input())))


