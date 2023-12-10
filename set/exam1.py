
# ''' Домашнее задание '''
#
# n, m, k, p = [int(input()) for _ in range(4)]
# res = n - (m + k - p)
# print(res)


# ''' Восход '''
#
# n = input().split()
# print(len(n) - len(set(n)))



''' Города '''

# n = int(input())
# t = [input() for _ in range(n)]
# new_t = input()
# if new_t in t:
#     print('REPEAT')
# else:
#     print('OK')
#
#
# ''' or '''
#
# set_set = {input() for _ in range(int(input()))}
# print('REPEAT' if input() in set_set else 'OK')


#
# ''' Книги на прочтение '''
#
# m, n = int(input()), int(input())
# m_book = set(input() for _ in range(m))
# n_book = [input() for _ in range(n)]
#
# for book in n_book:
#     if book in m_book:
#         print('YES')
#     else:
#         print('NO')
#
#
#
# ''' or '''
#
# m, n = int(input()), int(input())
# libr = {input() for _ in range(m)}
#
# for _ in range(n):
#     if input() in libr:
#         print('YES')
#     else:
#         print('NO')
#
#
#
# ''' or '''
#
# m, n = int(input()), int(input())
# mb = {input() for _ in range(m)}
# nb = [input() for _ in range(n)]
# [print(('NO', 'YES')[i in mb]) for i in nb]



#
# ''' Странное увлечение '''
#
#
# n, m = set(input().split()), set(input().split())
# intersection_set = n.intersection(m)
#
# if len(intersection_set) == 0:
#     print('BAD DAY')
# else:
#     sorted_intersection = sorted(intersection_set, key=int, reverse=True)
#     print(*sorted_intersection)
#
#
#
# ''' or '''
#
# set1 = {int(i) for i in input().split()}
# set2 = {int(i) for i in input().split()}
#
# if set1.isdisjoint(set2):
#     print('BAD DAY')
# else:
#     print(*sorted(set1 & set2, reverse=True))



# ''' Онлайн-школа BEEGEEK 1 '''
#
# set1 = {int(i) for i in input().split()}
# set2 = {int(i) for i in input().split()}
#
# if set1 == set2:
#     print('YES')
# else:
#     print('NO')
#
#
# ''' or '''
#
#
# print(('NO', 'YES')[set(input().split()) == set(input().split())])
#
#
# ''' or '''
# a = set(int(i) for i in input().split())
# b = set(int(i) for i in input().split())
# print('YES' if a == b else 'NO')



#
# ''' Онлайн-школа BEEGEEK 2 '''
#
#
# m = int(input())
# n = int(input())
#
# # Ввод фамилий учеников, изучающих математику
# math_students = {input() for _ in range(m)}
#
# # Ввод фамилий учеников, изучающих информатику
# informatics_students = {input() for _ in range(n)}
#
# # Находим учеников, изучающих только математику
# only_math_students = math_students - informatics_students
#
# # Выводим количество учеников, изучающих только математику
# print(len(only_math_students))
#
#
# ''' or '''
#
#
# m, n = int(input()), int(input())
# mat = {input() for _ in range(m)}
# inf = {input() for _ in range(n)}
#
# print(len(mat - inf))
#
#
# ''' or '''
#
#
# m, n = int(input()), int(input())
# a = set(input() for _ in range(m))
# b = set(input() for _ in range(n))
# print(len(a-b))




# ''' Онлайн-школа BEEGEEK 3 '''
#
#
# m = int(input())
# n = int(input())
#
# # Ввод фамилий учеников, изучающих математику
# math_students = {input() for _ in range(m)}
#
# # Ввод фамилий учеников, изучающих информатику
# informatics_students = {input() for _ in range(n)}
#
# # Находим учеников, изучающих только один предмет
# only_one_subject_students = (math_students | informatics_students) - (math_students & informatics_students)
#
# # Выводим количество учеников, изучающих только один предмет, или 'NO', если таких учеников нет
# if only_one_subject_students:
#     print(len(only_one_subject_students))
# else:
#     print('NO')
#
#
#
# ''' or '''
#
#
# m, n = int(input()), int(input())
# math = {input() for _ in range(m)}
# inf = {input() for _ in range(n)}
# result = len(math ^ inf)
#
# if result:
#     print(result)
# else:
#     print('NO')
#
#
#
# ''' or '''
#
#
# m, n = int(input()), int(input())
# mathematics = {input() for _ in range(m)}
# informatics = {input() for _ in range(n)}
#
# print(len(mathematics ^ informatics) or 'NO')




# ''' Онлайн-школа BEEGEEK 4 '''
#
#
# # Ввод фамилий учеников, записанных руководителем
# leader_input = input().split()
#
# # Ввод фамилий учеников, записанных помощником руководителя
# assistant_input = input().split()
#
# # Объединение списков и сортировка в лексикографическом порядке
# all_students = sorted(set(leader_input + assistant_input))
#
# # Вывод отсортированных фамилий
# print(*all_students)
#
#
#
# ''' or '''
#
# print(*sorted(set(input().split()) | set(input().split())))
#
# ''' or '''
#
# m = input().split()
# n = input().split()
# print(*sorted(set(m+n)))



# ''' Онлайн-школа BEEGEEK 5 🌶️ '''
#
#
# m, n = int(input()), int(input())
# stud_spis = [input() for _ in range(n + m)]
# stud_set = set(stud_spis)
# stud_less = len(stud_spis) - len(stud_set)
#
# if len(stud_set) - stud_less == 0:
#     print('NO')
# else:
#     print(len(stud_set) - stud_less)
#
#
# ''' or '''
#
# m, n = int(input()), int(input())
# set_all = {input() for _ in range(m + n)}
# print(['NO', 2 * len(set_all) - (m + n)][2 * len(set_all) != m + n])
#
#
# ''' or '''
#
#
# m,n = int(input()), int(input())
# a = [input() for _ in range(m+n)]
# k = set(a)
# l = len(k) - (len(a) - len(k))
# if  l > 0:
#     print(l)
# else:
#     print("NO")


# ''' Онлайн-школа BEEGEEK 6 🌶️ '''
#
#
# m = int(input())
#
# # Словарь для хранения учеников на каждом уроке
# lesson_attendance = {}
#
# # Ввод фамилий учеников для каждого урока
# for i in range(m):
#     n = int(input())
#     for _ in range(n):
#         student = input()
#         lesson_attendance.setdefault(student, set()).add(i)
#
# # Находим учеников, присутствовавших на всех уроках
# all_lessons_set = set(range(m))
# all_lessons_students = [student for student, lessons in lesson_attendance.items() if lessons == all_lessons_set]
#
# # Вывод результатов
# for student in sorted(all_lessons_students):
#     print(student)
#
#
#
# ''' or '''
#
# n = int(input())
# result = {input() for _ in range(int(input()))}
#
# for _ in range(n - 1):
#     result &= {input() for _ in range(int(input()))}
#
# print(*sorted(result), sep='\n')
#
#
# ''' or '''
#
# s = [set(input() for _ in range(int(input()))) for _ in range(int(input()))]
# print(*sorted(set.intersection(*s)), sep='\n')


