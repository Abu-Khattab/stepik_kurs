# ''' создает, заполняет и возвращает матрицу заданного размера '''
#
# def matrix(n=1, m=None, v=0):
#     if n == 1 and m is None:
#         m = 1
#     elif n != 1 and m is None:
#         m = n
#     return [[v] * m for _ in range(n)]
#
#
# print(matrix())         # матрица 1 × 1 из 0
# print(matrix(3))        # матрица 3 × 3 из 0
# print(matrix(2, 5))     # матрица 2 × 5 из 0
# print(matrix(3, 4, 9))  # матрица 3 × 4 из 9
#
# #
# ''' or '''
#
# def matrix(n=1, m=None, value=0):
#     if m is None:
#         m = n
#     return [[value] * m for _ in range(n)]
#
#
# print(matrix())         # матрица 1 × 1 из 0
# print(matrix(3))        # матрица 3 × 3 из 0
# print(matrix(2, 5))     # матрица 2 × 5 из 0
# print(matrix(3, 4, 9))  # матрица 3 × 4 из 9
#
#
# ''' or '''
#
# def matrix(n=1, m=0, value=0):
#     return [[value for _ in range(m if m else n)] for _ in range(n)]
#
#
# print(matrix())         # матрица 1 × 1 из 0
# print(matrix(3))        # матрица 3 × 3 из 0
# print(matrix(2, 5))     # матрица 2 × 5 из 0
# print(matrix(3, 4, 9))  # матрица 3 × 4 из 9
#


# ''' фунция имитации пространства имен переменных '''
#
#
# n = int(input())
# variables = {"global": {"parent": None, "variables": set()}}
#
# def add_variable(namespace, var):
#     variables[namespace]["variables"].add(var)
#
# def find_namespace(namespace, var):
#     if var in variables[namespace]["variables"]:
#         return namespace
#     if namespace == "global":
#         return None
#     return find_namespace(variables[namespace]["parent"], var)
#
# results = []
#
# for _ in range(n):
#     command, namespace, arg = input().split()
#     if command == "create":
#         parent_namespace = arg
#         variables[namespace] = {"parent": parent_namespace, "variables": set()}
#     elif command == "add":
#         add_variable(namespace, arg)
#     elif command == "get":
#         results.append(find_namespace(namespace, arg))
#
# for result in results:
#     print(result)
#


# ''' принимает произвольное количество аргументов и возвращает среднее арифметическое
# переданных в нее числовых (int или float) аргументов'''
#
# def mean(*args):
#     numeric_args = [i for i in args if type(i) in (int, float)]
#     if not numeric_args:
#         return 0.0
#     return sum(numeric_args) / len(numeric_args) if len(numeric_args) > 0 else 0
#
# print(mean())  # Вывод: 0.0
# print(mean(7))  # Вывод: 7.0
# print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))  # Вывод: 1.6666666666666667
# print(mean(True, ['stepik'], 'beegeek', (1, 2)))  # Вывод: 1.0
# print(mean(-1, 2, 3, 10, ('5')))  # Вывод: 3.5
# print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) # Вывод: 5.5
#
#
# ''' or '''
#
# def mean(*args):
#     numeric_args = [i for i in args if type(i) in (int, float)]
#     if numeric_args:
#         return sum(numeric_args) / len(numeric_args)
#     else:
#         return 0.0
#
# print(mean())
# print(mean(7))
# print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
# print(mean(True, ['stepik'], 'beegeek', (1, 2)))
# print(mean(-1, 2, 3, 10, ('5')))
# print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# ''' or '''
#
# def mean(*args):
#     a = [i for i in args if type(i) in (int, float)]
#     return sum(a) / len(a) if a else 0


# ''' Передача аргументов в форме списка и кортежа '''
#
#
# def my_sum(*args):
#     return sum(args)
#
#
# print(my_sum(*[1, 2, 3, 4, 5, 10]))  # распаковка списка
# print(my_sum(*(1, 2, 3) + (5, 5)))
#
# ''' Получение именованных аргументов в виде словаря '''
#
#
# def my_func(**kwargs):
#     print(kwargs)
#
#
# my_func()
# my_func(a=1, b=2)
# my_func(name='Timur', job='Teacher')


# ''' Передача именованных аргументов в форме словаря '''
#
#
# def my_func(**kwargs):
#     print(kwargs)
#
#
# info = {'name': 'Timur', 'age': '28', 'job': 'teacher'}
#
# my_func(**info)


# ''' or '''
#
# def print_info(name, surname, age, city, *children, **additional_info):
#     print('Имя:', name)
#     print('Фамилия:', surname)
#     print('Возраст:', age)
#     print('Город проживания:', city)
#     if len(children) > 0:
#         print('Дети:', ', '.join(children))
#     if len(additional_info) > 0:
#         print(additional_info)
#
#
# children = ['Бодхи Рансом Грин', 'Ноа Шэннон Грин', 'Джорни Ривер Грин']
# additional_info = {'height':163, 'job':'actress'}
#
# print_info('Меган', 'Фокс', 34, 'Ок-Ридж', *children, **additional_info)


# ''' возвращает приветствие '''
#
# def greet(name, *args):
#     return f'Hello, {" and ".join((name,) + args)}!'
#
#
# print(greet('Timur'))
# print(greet('Timur', 'Roman'))
# print(greet('Timur', 'Roman', 'Ruslan'))
#
#
# ''' or '''
#
# def greet(first_name, *other_names):
#     if other_names:
#         return f"Hello, {first_name} and {' and '.join(other_names)}!"
#     else:
#         return f"Hello, {first_name}!"
#
#
# print(greet('Timur'))
# print(greet('Timur', 'Roman'))
# print(greet('Timur', 'Roman', 'Ruslan'))


# ''' выводит список продуктов '''
#
# def print_products(*args):
#     res = [product for product in args if isinstance(product, str) and product.strip()]
#     result = []
#     for index, fruit in enumerate(res, start=1):
#         result.append(f"{index}) {fruit}")
#     if not result:
#         result.append("Нет продуктов")
#     return '\n'.join(result)
#
#
# print(print_products([4], {}, 1, 2, {'Beegeek'}, ''))
# print(print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True))
#
#
# ''' or '''
#
# def print_products(*a):
#     count = 1
#     for i in a:
#         if type(i) is str and i:
#             print(f'{count}) {i}')
#             count += 1
#     if count == 1:
#         print('Нет продуктов')
#
#
# print(print_products([4], {}, 1, 2, {'Beegeek'}, ''))
# print(print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True))
#
#
#
# ''' or '''
#
# def print_products(*args):
#     result = [i for i in args if type(i) is str and i]
#     return [print(f'{num}) {food}') for num, food in enumerate(result, 1)] if result else print('Нет продуктов')
#
#
# print_products([4], {}, 1, 2, {'Beegeek'}, '')
# print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
#
#
# ''' or '''
#
# def print_products(*args):
#     ls = [i for i in args if isinstance(i, str) and i not in ('', ' ')]
#     print('\n'.join([f'{num}) {i}' for num, i in enumerate(ls, 1)]) if ls else 'Нет продуктов')
#
#
#
# print_products([4], {}, 1, 2, {'Beegeek'}, '')
# print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)


# ''' печатает именованные аргументы '''
#
# def info_kwargs(**kwargs):
#     sorted_kwargs = sorted(kwargs.items())
#     for i, j in sorted_kwargs:
#         print(f'{i}: {j}')
#
#
# info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')
#
#
#
# ''' or '''
#
# def info_kwargs(**kwargs):
#     [print(f'{key}: {kwargs[key]}') for key in sorted(kwargs.keys())]
#
#
# info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')
#
#
# ''' or '''
#
# def info_kwargs(**kwargs):
#     for k, v in sorted(kwargs.items()):
#         print(f'{k}: {v}')


# ''' минимальное и максимальное среднее арифметическое значение элементов. '''
#
# numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2),
#            (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]
#
# # Функция для вычисления среднего арифметического
# def average(tup):
#     return sum(tup) / len(tup)
#
# # Находим кортеж с минимальным средним арифметическим
# min_tuple = min(numbers, key=average)
#
# # Находим кортеж с максимальным средним арифметическим
# max_tuple = max(numbers, key=average)
#
# # Выводим результаты
# print(min_tuple)
# print(max_tuple)


# ''' с суммой минимального и максимального элемента кортежа '''
#
#
# numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34),
#            (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]
#
#
# def com(x):
#     return min(x) + max(x)
#
#
# numbers.sort(key=com)
# print(numbers)
#
#
# ''' or '''
#
# numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]
# numbers.sort(key=lambda i: min(i) + max(i))
#
#
# print(numbers)


# ''' Сортируй как хочешь '''
#
# athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30),
#             ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
#
#
# def comparator_i(i):
#     def comparator(pair):
#         return pair[n - 1]
#
#     return comparator
#
#
# n = int(input())
#
# for i in sorted(athletes, key=comparator_i(n)):
#     print(*i, end='\n')
#
# comparator_i(athletes)
#
#
# ''' or '''
#
# athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
#
# def sort_name(athlete):
#     return athlete[0]
#
#
# def sort_age(athlete):
#     return athlete[1]
#
#
# def sort_height(athlete):
#     return athlete[2]
#
#
# def sort_weight(athlete):
#     return athlete[3]
#
# sort_by = {1: sort_name, 2: sort_age, 3: sort_height, 4: sort_weight}
#
# for i in sorted(athletes, key=sort_by[int(input())]):
#     print(*i)



# ''' Математические функции '''
#
#
# from math import sin
#
# commands = {'квадрат': lambda x: x ** 2,
#             'куб': lambda x: x ** 3,
#             'корень': lambda x: x ** 0.5,
#             'модуль': lambda x: abs(x),
#             'синус': lambda x: sin(x)}
#
# n = int(input())
# s = input()
#
# operation = commands.get(s)
# if operation:
#     result = operation(n)
#     print(result)
# else:
#     print("Операция не найдена")
#
#
#
# ''' or '''
#
# from math import sin
#
# def math_func(n, f):
#     return {'квадрат': n**2, 'куб': n**3, 'корень': n**0.5, 'модуль': abs(n), 'синус': sin(n)}[f]
#
# print(math_func(int(input()), input()))  # число, команда
#
#
# ''' or '''
#
# from math import sin
#
#
# def square(x):
#     return x ** 2
#
#
# def cube(x):
#     return x ** 3
#
#
# def square_root(x):
#     return x ** 0.5
#
#
# def module(x):
#     return abs(x)
#
#
# def sinus(x):
#     return sin(x)
#
#
# functions = {'квадрат': square, 'куб': cube, 'корень': square_root,
#              'модуль': module, 'синус': sinus}
#
# n, func = int(input()), input()
# print(functions[func](n))



# ''' Интересная сортировка-1 '''
#
# def fun(x):
#     x = [int(i) for i in str(x)]
#     return sum(x)
#
#
# n = input().split()
# print(*sorted(n, key=fun))


# ''' Интересная сортировка-2 '''
#
# def fun(x):
#     x = [int(i) for i in str(x)]
#     return sum(x)
#
#
# n = input().split()
# a = sorted(n, key=int)
# print(*sorted(a, key=fun))




# ''' сортирует список points координат '''
#
# points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]
# points.sort(key=lambda x: x[0]**2 + x[1]**2)
# print(points)
#
#
#
# ''' or '''
#
# points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0),
#           (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]
#
#
# def distance(point):
#     return (point[0] ** 2 + point[1] ** 2) ** 0.5
#
#
#
# points.sort(key=distance)
# print(points

