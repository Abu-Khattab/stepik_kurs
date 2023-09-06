# ''' f-строки '''
#
# first_name = 'Timur'
# last_name = 'Guev'
# age = 27
# profession = 'math teacher'
# affiliation = 'BeeGeek'
# print('Hello, {0} {1}. You are {2}. You are a {3}. You were a member of {4}'
#                .format(first_name, last_name, age, profession, affiliation))
#
#
# first_name = 'Timur'
# last_name = 'Guev'
# age = 27
# profession = 'math teacher'
# affiliation = 'BeeGeek'
# print(f'Hello, {first_name} {last_name}. You are {age}. You are a {profession}. You were a member of {affiliation}')


# s = 'In {0}, someone paid {1} {2} for two pizzas.'.format(2010, '10k', 'Bitcoin')
# print(s)


# year = 2010
# amount = '10K'
# currency = 'Bitcoin'
#
# print(f'In {year}, someone paid {amount} {currency} for two pizzas.')


# ''' код для вывода всех заглавных букв английского алфавита'''
#
# for i in range(26):
#     print(chr(ord('A') + i))



# ''' Символы в диапазоне '''
#
# a, b = int(input()), int(input())
# for i in range(a, b + 1):
#     print(chr(i), end=' ')


# ''' Простой шифр '''
#
# s = input()
# for i in s:
#     print(ord(i), end=' ')


# ''' Шифр Цезаря 🌶️ '''
#
# sdvig, sms = int(input()), input()
# for i in range(len(sms)):
#     n = ord(sms[i]) - sdvig
#     if n < 97:
#         n = 122 - (96 - n)
#     print(chr(n), end='')


# ''' или '''
#
# n = int(input())
# a = input()
#
# for i in a:
#     k = ord(i)-n
#     if k < 97:
#         k = k + 26
#     print(chr(k), end = '')


