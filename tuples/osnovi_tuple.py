''' tuples '''

# colors = ('red', ('green', 'blue'), 'yellow')
# numbers = (1, 2, (4, (6, 7, 8, 9)), 10, 11)
# print(colors[1][1])
# print(numbers[2][1][3])



# ''' minimum value and maximum value '''

# numbers = (12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324)
#
# print(min(numbers), max(numbers))


# countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy')
# index = countries.index('Slovenia')
# print(index)



# ''' только непустые кортежи исходного списка  '''
#
# tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
# non_empty_tuples = [i for i in tuples if i]
#
# print(non_empty_tuples)


# ''' содержала список кортежей на основе списка tuples с последним элементом каждого кортежа,
#     замененным на численное значение 100 '''
#
# tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
# new_tuples = [i[:-1] + (100,) for i in tuples]
# print(new_tuples)



# notes = ('Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si')
# string1 = ''.join(notes)
# string2 = '--'.join(notes)
#
# print(string1)
# print(string2)


# letters = 'abcdefghijkl'
# tpl = tuple(letters)
# print(tpl)


# number = 12345
# string = str(number)
# tpl = tuple(string)
# print(*tpl)



# ''' bable sort '''
#
# poets = [
#     ('Есенин', 13),
#     ('Тургенев', 14),
#     ('Маяковский', 28),
#     ('Лермонтов', 20),
#     ('Фет', 15)]
#
# for i in range(len(poets)):
#     for j in range(i+1, len(poets)):
#         if poets[i][1] > poets[j][1]:
#             poets[i], poets[j] = poets[j], poets[i]
#
# print(poets[0])
# print(poets[-1])


# ''' Кортежи сравниваются поэлементно. оно сравнивает имена лексикографически
#     (что является алфавитным порядком по умолчанию). '''
#
# poets = [
#     ('Тургенев', 14),
#     ('Есенин', 13),
#     ('Маяковский', 28),
#     ('Фет', 15),
#     ('Лермонтов', 20)]
#
# for i in range(len(poets)):
#     for j in range(i+1, len(poets)):
#         if poets[i] > poets[j]:
#             poets[i], poets[j] = poets[j], poets[i]
#
# print(poets[0])
# print(poets[-1])



# ''' произведение элементов кортежа numbers. '''
#
# numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
# counter = 1
# for i in numbers:
#     counter *= i
# print(counter)


# ''' вписываем значение в канец кортежа '''

# poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
# poet_data = list(poet_data)
# poet_data[-1] = 'Москва'
#
# print(poet_data)

# ''' or '''
#
# poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
# poet_data = poet_data[:-1] + ('Москва',)
#
# print(poet_data)


# ''' or '''
#
# poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
# poet_data = tuple(list(poet_data)[:-1]+['Москва'])
#
# print(poet_data)



# ''' список, содержащий средние арифметические значения чисел каждого вложенного кортежа
#     в заданном кортеже кортежей numbers.'''
#
#
# numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
#
# li = []
# for i in numbers:
#     total = 0
#     for j in i:
#         total += j  # Мы суммируем значения j, не используя sum()
#
#     average = total / len(i)  # Вычисляем среднее для каждой кортежа
#     li.append(average)
# print(li)
#
#
#
# ''' or '''
#
#
# numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
#
# print([sum(i) / len(i) for i in numbers])
#
#
#
# ''' or '''
#
#
# numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
# l = []
# for i in numbers:
#   l.append(sum(i) / len(i))
#
# print(l)



# ''' Программа должна вывести координаты вершины параболы по формуле  '''
#
# a, b, c = int(input()), int(input()), int(input())
# x_vertex = -b / (2 * a)
# y_vertex = c - (b ** 2) / (4 * a)
# print((x_vertex, y_vertex))


# ''' or '''
#
# def parabola_vertex(a, b, c):
#     x = -(b / (2 * a))
#     y = (4 * a * c - b**2) / (4 * a)
#     return x, y
#
#
# print(parabola_vertex(int(input()), int(input()), int(input())))



# ''' выводит список хорошистов и отличников в классе '''


# n = int(input("Введите количество учеников: "))
#
# # Создаем списки для всех учеников, хорошистов и отличников
# all_students = []
# good_students = []
# excellent_students = []
#
# # Считываем информацию о каждом ученике
# for _ in range(n):
#     student_info = input("Введите фамилию и оценку через пробел: ").split()
#     name = student_info[0]
#     grade = int(student_info[1])
#
#     # Добавляем информацию в список всех учеников
#     all_students.append((name, grade))
#
#     # Проверяем оценку и добавляем ученика в соответствующий список
#     if grade >= 4:
#         good_students.append((name, grade))
#     if grade == 5:
#         excellent_students.append((name, grade))
#
# # Выводим все учеников
# for student in all_students:
#     print(f"{student[0]} {student[1]}")
#
# # Выводим пустую строку
# print()
#
# # Выводим хорошистов и отличников
# for student in good_students:
#     print(f"{student[0]} {student[1]}")
#
#
# ''' or '''
#
# students = [tuple(input().split()) for _ in range(int(input()))]
#
# for student in students:
#     print(*student)
#
# print()
#
# for name, grade in students:
#     if int(grade) > 3:
#         print(name, grade)
#
#
#
#
# ''' or '''
#
# pup = [input() for _ in range(int(input()))]
# print(*pup, sep='\n')
# print()
# [print(x) for x in pup if int(x[-1]) > 3]






# ''' вычисление чисел Фибоначчи'''
#
# n = int(input())
# f1, f2 = 1, 1
# for i in range(n):
#     print(f1)
#     f1, f2 = f2, f1 + f2




# ''' вычисление чисел трибоначчи'''
#
# n = int(input())
# f1, f2, f3 = 1, 1, 1
# for i in range(n):
#     print(f1, end=' ')
#
#     f1, f2, f3 = f2, f3, f1 + f2 + f3

