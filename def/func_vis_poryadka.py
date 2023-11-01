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


