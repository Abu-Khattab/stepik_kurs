
# ''' сумма квадратов элементов списка '''
#
# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# total = 0
# for num in numbers:
#     total += num * num
# print(total)


# ''' для каждого введенного числа
# x выводит значение функции '''
#
# res = []
# counter = []
# for i in range(1, int(input()) + 1):
#     n = int(input())
#     counter.append(n)
#     res.append(n ** 2 + 2 * n + 1)
# print(*counter, sep='\n')
# print('')
# print(*res, sep='\n')


# ''' удаляет наименьшее и наибольшее значение из указанных чисел '''
#
# li = []
# for i in range(int(input())):
#     n = int(input())
#     li.append(n)
# li.remove(max(li))
# li.remove(min(li))
# print(*li, sep='\n')

# ''' или Без del и без index '''
#
# n, l = int(input()), []
# for i in range(n):
#   l.append(int(input()))
# for a in l:
#   if a != min(l) and a != max(l):
#     print(a)


# ''' выводит только уникальные строки, в том же порядке '''
#
# li = []
# for i in range(int(input())):
#     s = input()
#     if s not in li:
#         li.append(s)
# print(*li, sep='\n')



# ''' выводит все введенные строки, в которых встречается поисковый запрос. '''
#
# li = []
# for _ in range(int(input())):
#     li.append(input())
# search = input()
# for i in li:
#     if search.lower() in i.lower():
#         print(i)


# ''' сначала выводит все отрицательные числа, затем нули,
#  а затем все положительные числа '''
#
# num = []
# num2 = []
# num3 = []
# for _ in range(int(input())):
#     n = int(input())
#     if n < 0:
#         num.append(n)
#     if n == 0:
#         num2.append(n)
#     if n > 0:
#         num3.append(n)
#
# print(*num, *num2, *num3, sep='\n')

# ''' или '''
#
# negatives, zeros, positives = [], [], []
#
# n = int(input())
# for _ in range(n):
#     cur = int(input())
#     if cur < 0:
#         negatives.append(cur)
#     elif cur > 0:
#         positives.append(cur)
#     else:
#         zeros.append(cur)
#
# res = negatives + zeros + positives
# print(*res, sep="\n")
#
#
# ''' или '''
#
# n = int(input())
# x = [int(input()) for _ in range(n)]
# [print(i) for i in x if i < 0]
# [print(i) for i in x if i == 0]
# [print(i) for i in x if i > 0]


# ''' Google search - 2 🌶️🌶️ '''
#
# li, li2 = [], []
# n = int(input())
#
# for _ in range(n):
#     li.append(input())
#
# k = int(input())
# for _ in range(k):
#     li2.append(input())
#
# for i in range(n):
#     counter = 0
#     for q in range(k):
#         if li2[q].lower() in li[i].lower():
#             counter += 1
#     if counter == k:
#         print(li[i])
#     counter = 0
#
#
#
# ''' или '''
#
# s = [input() for _ in range(int(input()))]
# d = [input() for _ in range(int(input()))]
# for i in s:
#     for j in d:
#         if j.lower() not in i.lower():
#             break
#     else:
#         print(i)