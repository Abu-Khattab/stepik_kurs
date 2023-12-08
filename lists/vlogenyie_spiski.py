# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
#
# print(list1)


# list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
# sub_list = ['h', 'i', 'j']
# list1[2][1][2].extend(sub_list)
# print(list1)


# list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# maximum = -1
# for i in list1:
#     for j in i:
#         if j > maximum:
#             maximum = j
# print(maximum)
#
#
# ''' or '''
#
# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# maximum = -1
#
# for li in list1:
#     if max(li) > maximum:
#         maximum = max(li)
# print(maximum)
#
# ''' or '''
#
# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# maximum = max(map(max, list1))
#
# print(maximum)


# ''' or '''
#
# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# maximum = -1
# print(max(j for i in list1 for j in i))


# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
#
# list1 = [i[::-1] for i in list1]
# print(list1)
#
#
# ''' or '''
#
# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# [x.reverse() for x in list1]
# print(list1)


# ''' сумму всех чисел списка list1, разделённую на общее количество всех чисел. '''

# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# total = 0
# counter = 0
#
# for i in list1:
#     for j in i:
#         total += j
#         counter += 1
# print(total / counter)
#
#
# ''' or '''
#
# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# total = sum([sum(i) for i in list1])
# counter = sum([len(i) for i in list1])
# print(total / counter)
#
#
# ''' or '''
#
# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# total = 0
# counter = 0
#
# for li in list1:
#     total += sum(li)
#     counter += len(li)
#
# print(total / counter)
#
#
# ''' or '''
#
# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# total = sum(map(sum, list1))
# counter = sum(map(len, list1))
# print(total / counter)


# ''' or '''

# '''  Зачем же в функции SUM второй аргумент? Мало кто вообще про него знает :)
#     Он указывает значение, к которому следует суммировать все элементы из iterable.'''
#
# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# flat_list = sum(list1, [])
# print(sum(flat_list) / len(flat_list))


# my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# for i in my_list:
#     print(*i)

#
# ''' Список по образцу 1 '''
#
# n = int(input())
# my_list = [[j for j in range(1, n + 1)]for i in range(n)]
# for row in my_list:
#     print(row)
#
# ''' or '''
#
# n = int(input())
# result = []
#
# for _ in range(n):
#     result.append(list(range(1, n + 1)))
#
# print(*result, sep='\n')
#
#
# ''' or '''
#
# n = int(input())
# print(*[[i for i in range(1, n+1)] for i in range(1, n+1)], sep = "\n")
#
#
# ''' or '''
#
# n = int(input())
# for _ in range(n):
#     print(list(range(1, n + 1)))


# n = int(input())
# for i in range(1, n + 1):
#     print(list(range(1, i+1)))


# ''' Треугольник Паскаля 1 🌶️ '''
#
# n = int(input())
# p = [[1]]
# for i in range(1, n + 1):
#     row = [1] * (i + 1)
#     for j in range(i + 1):
#         if j != 0 and j != i:
#             row[j] = p[i-1][j-1] + p[i-1][j]
#
#     p.append(row)
# print(p[-1])
#
#
#
# ''' or '''
#
# from math import factorial
# n = int(input())
# b = []
# for i in range(n+1):
#     b.append (int((factorial(n))/(factorial(i)*factorial(n-i))))
# print(b)
#
#
# ''' or '''
#
# n = int(input())
#
# li = [1]
# for i in range(n):
#     for j in range(len(li) - 1):
#         li[j] = li[j] + li[j + 1]
#     li.insert(0, 1)
#
# print(li)


# ''' Треугольник Паскаля 2 '''
#
# n = int(input())
# p = []
# for i in range(n):
#     row = [1] * (i + 1)
#     for j in range(i + 1):
#         if j != 0 and j != i:
#             row[j] = p[i-1][j-1] + p[i-1][j]
#
#     p.append(row)
#
# for r in p:
#     print(*r)
#
#
# ''' or '''
#
# pasc = [1]
# for x in range(int(input())):
#     print(*pasc)
#     pasc[1:] = list(map(lambda a, b: a + b, pasc, pasc[1:] + [0]))
#
#
#
# ''' or '''
#
# from math import factorial
#
# n = int(input())
#
# for j in range(n):
#     l = [int(factorial(j)/(factorial(i) * factorial(j - i))) for i in range(j + 1)]
#     print(*l)


# ''' Упаковка дубликатов 🌶️ '''
#
# from itertools import groupby
#
# s = input().split()
# result = [list(group) for key, group in groupby(s)]
# print(result)
#
#
#
# ''' or '''
#
# res = []
#
# for el in input().split():
#     if res and el in res[-1]:
#         res[-1].append(el)
#     else:
#         res.append([el])
#
# print(res)
#
#
#
# ''' or '''
#
# res = []
# a = input().split()
# for i in a:
#     res.append([i]) if not res or i not in res[-1] else res[-1].append(i)
# print(res)
#
#
# ''' or '''
#
# s = input().split()
# # кидаем первый символ в наш список, также удалив его из входного списка
# seq = [[s.pop(0)]]
#
# for c in s:
#     if c in seq[-1]:
#         seq[-1].append(c)
#     else:
#         seq.append([c])
#
# print(seq)



# ''' Разбиение на чанки 🌶️ '''
#
# def chunked(chars, num):
#     chunked_list = []
#     for i in range(0, len(chars), num):
#         chunk = chars[i: i + num]
#         chunked_list.append(chunk)
#     return chunked_list
#
#
# a, b = input().split(), int(input())
# chunks = chunked(a, b)
# print(chunks)
#
#
# ''' or '''
#
# a = input().split()
# b = int(input())
# print([a[i:i + b] for i in range(0, len(a), b)])



# ''' Подсписки списка 🌶️🌶️ '''
#
# a = input().split()
# c = []
#
# for i in range(len(a)):
#     for j in range(len(a) - i):
#         b = a[j:j+i+1]
#         c.append(b)
#
# print(c)


