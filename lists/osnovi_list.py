# ''' Список чисел '''
#
# n = int(input())
# numbers = list(range(1, n + 1))
# print(numbers)



# n = int(input())
# abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
#        'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# print(abc[:n])

# ''' или '''

# n = int(input())
# s = ''
# for i in range(n):
#     s += chr(ord("a") + i)
# print(list(s))


# ''' или '''
#
# n = int(input())
# s = ''
# for i in range(n):
#     s += chr(97 + i)
# print(list(s))


# ''' Замена элементов списка '''
#
# rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
#
# rainbow[3] ='Зеленый'
# rainbow[-1] ='Фиолетовый'
#
# print(rainbow)
#
# ''' или '''
#
# rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
# rainbow[3::3] = ['Зеленый', 'Фиолетовый']
# print(rainbow)
#
# ''' или '''
#
# rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
# rainbow[rainbow.index('Green')] = 'Зеленый'
# rainbow[rainbow.index('Violet')] = 'Фиолетовый'
# print(rainbow)


# ''' в обратном порядке '''
#
#
# languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
# print(languages[::-1])
#
#
# ''' или '''
#
# languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
# languages.reverse()
# print(languages)



# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# del numbers[::2]
#
# print(numbers)


# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10,
# 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
#
# print(len(numbers))
# print(numbers[-1])
# print(numbers[::-1])
# if 5 in numbers and 17 in numbers:
#     print('YES')
# else:
#     print('NO')
# del numbers[0]
# del numbers[-1]
# print(numbers)


# '''создает из указанных строк список и выводит его.'''

# n = int(input())
# l = []
# for i in range(n):
#     s = input()
#     l.append(s)
# print(l)

# '''Или таким'''
#
# n = int(input())
# lst = [input() for _ in range(n)]
# print(lst)
#
#
# '''Или таким'''
#
# n = int(input())
# print([input() for _ in range(n)])
#
#
# '''Или вообще таким'''
#
# print([input() for _ in range(int(input()))])


# ''' оследний элемент списка состоит из 26 символов z '''
#
# abc = 'abcdefghijklmnopqrstuvwxyz'
# n = 26
# output_list = [abc[i] * (i + 1) for i in range(n)]
# print(output_list)
#
#
# ''' или '''
#
# res = []
# for i in range(26):
#     cur = ""
#     for j in range(i + 1):
#         cur += chr(ord("a") + i)
#
#     res.append(cur)
#
# print(res)
#
#
# ''' или '''
#
# print([chr(97 + i) * (i + 1) for i in range(26)])

# ''' юникод '''
#
# for i in range(26):
#     print(chr(ord('a') + i))
#
#
# for i in range(26):
#     print(ord('a') + i)


# ''' создает из указанных чисел список их кубов '''
#
# n = int(input())
# res = []
# for _ in range(n):
#     n1 = int(input())
#     res.append(n1 ** 3)
# print(res)


# ''' или '''
#
# print([int(input()) ** 3 for i in range(int(input()))])


# '''создает список, состоящий из делителей введенного числа.'''
#
# n = int(input())
# lis = []
# for i in range(1, n + 1):
#     if n % i == 0:
#         lis.append(i)
# print(lis)

# ''' или '''
#
# n = int(input())
# print([i for i in range(1, n + 1) if n % i == 0])


# ''' Суммы двух '''
#
# n = int(input())
# lis = []
# lis2 = []
# for i in range(n):
#     iter = int(input())
#     lis.append(iter)
# for j in range(len(lis) - 1):
#     lis2.append(lis[j] + lis[j+1])
# print(lis2)


# ''' или '''
#
# n, a = int(input()), int(input())
# lst = []
# for _ in range(n-1):
#     b = int(input())
#     lst.append(a + b)
#     a = b
# print(lst)

# ''' или '''
#
# seq = []
# for _ in range(int(input())):
#     seq.append(int(input()))
#
# res = []
# for i in range(len(seq) - 1):
#     res.append(seq[i] + seq[i + 1])
#
# print(res)



# ''' создает из указанных чисел список, затем удаляет все элементы стоящие по нечетным индексам,
#  а затем выводит полученный список '''
#
# n, lis = int(input()), []
# for _ in range(n):
#     ite = int(input())
#     lis.append(ite)
# del lis[1::2]
# print(lis)
#
#
# ''' или '''
#
# n = int(input())
# seq = []
#
# for _ in range(n):
#     cur = int(input())
#     seq.append(cur)
#
# print(seq[::2])


# ''' создает список из символов всех строк, а затем выводит его. '''
#
# lis = []
# for i in range(int(input())):
#     n = input()
#     lis.extend(n)
# print(lis)
#
#
# ''' или '''
#
# print([c for _ in range(int(input())) for c in input()])



''' k-ая буква слова 🌶️🌶️ '''

# n = int(input())
# li = []
# for _ in range(n):
#     li.append(input())
# index = int(input())
# res = ''
# for s in li:
#     if len(s) >= index:
#         res += s[index - 1]
#
# print(res)


# ''' или '''
#
# n = int(input())
#
# seq = []
# for _ in range(n):
#     seq.append(input())
#
# k = int(input())
#
# res = ""
# for i in range(n):
#     if len(seq[i]) < k:
#         continue
#
#     res += seq[i][k - 1]
#
# print(res)

