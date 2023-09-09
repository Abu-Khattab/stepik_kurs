# ''' выводит слова введенной строки в столбик '''
#
# s = input().split()
# print(*s, sep='\n')


# ''' выводит инициалы человека. '''
#
# initials = input().split()
# res = ''
# for i in initials:
#     res += i[0]
# print('.'.join(res),'.', sep='')
#
#
# ''' или '''
#
# full_name = input().split()
# print(full_name[0][0], full_name[1][0], full_name[2][0], sep=".", end=".")
#
#
# ''' или '''
#
# s = input().split()
# for i in (s):
#     print(i[0], end=".")

# ''' или '''
#
# name = input().split()
# print(f'{name[0][0]}.{name[1][0]}.{name[2][0]}.')

# ''' разбирает строку на части, разделенные символом "\".
#     Каждую часть вывести в отдельной строке. '''
#
# s = input().split('\\')
# for i in s:
#     print(i)

# '''  которая по заданным числам строит столбчатую диаграмму. '''

# s = input().split()
# plus = []
# print(plus)
# for i in range(len(s)):
#     plus.append(s[i])
#     print(int(plus[-1]) * '+' )
#
#
# ''' или '''
#
# seq = input().split()
#
# for el in seq:
#     print("+" * int(el))
#
#
# ''' или '''
#
# for i in input().split():
#     print('+' * int(i))


# ''' определяет, является ли введенная строка текста корректным ip-адресом '''
#
# numbers = input().split('.')
# count = 0
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
#     if 0 <= numbers[i] <= 255:
#         count += 1
# if count == 4:
#     print("ДА")
# else:
#     print("НЕТ")
#
#
# ''' или '''
#
# seq = input().split(".")
#
# for el in seq:
#     if not (0 <= int(el) <= 255):
#         print("НЕТ")
#         break
# else:
#     print("ДА")
#
#
# ''' или '''
#
# s = input().split('.')
# for i in s:
#     if int(i) < 0 or int(i) > 255:
#         print('НЕТ')
#         break
# else:
#     print('ДА')
#
# ''' или '''
#
# flag = 'ДА'
# for c in input().split('.'):
#     if int(c) > 255:
#         flag = 'НЕТ'
# print(flag)


# ''' строка в качестве разделителя для join '''
#
# n, s = input(), input()
# print(s.join(n))



# ''' Количество совпадающих пар '''
#
# numbers = input().split()
# counter = 0
# for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):
#         if numbers[j] == numbers[i]:
#             counter += 1
#
# print(counter)


# ''' или '''
#
# a = input().split()
# s = 0
# for i in range(len(a) - 1):
#     s += a[i + 1:].count(a[i])
# print(s)