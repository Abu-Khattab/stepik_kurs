''' начало нового модуля list '''


# s = 'All you need is love'
# if 'love' in s:
#     print('❤️')
# else:
#     print('💔')


# s = 'abcdef'
# for i in range(len(s)):
#     print(s[i])



# s = 'abcdef'
# for c in s:
#     print(c)


# s = '01234567891011121314151617'
# for i in range(0, len(s), 5):
#     print(s[i], end='')


# s = input()
# for i in range(0, len(s), 2):
#     print(s[i])


# s = input()
# for i in range(1, len(s) + 1):
#     print(s[-i])


# s = input()
#
# for i in range(len(s) - 1, -1, -1):
#     print(s[i])


# i, f, o = input(), input(), input()
# print(f[0], i[0], o[0], sep='')


# s = input()
# su = 0
# for i in range(len(s)):
#     su += int(s[i])
# print(su, end='')


# s = input()
# sm = 0
#
# for digit in s:
#     sm += int(digit)
#
# print(sm)



# s = input()
# digit = '0123456789'
# counter = 0
# for i, row in enumerate(s):
#     if row in digit:
#         counter += 1
# if counter > 0:
#     print("Цифра")
# else:
#     print("Цифр нет")



# s = input()
# digits = '0123456789'
#
# for i in s:
#     if i in digits:
#         print('Цифра')
#         break
# else:
#     print('Цифр нет')


# ''' мой ответ '''

# s = input()
# counter = 0
# counter1 = 0
# for i in range(len(s)):
#     if s[i] == '*':
#         counter += 1
#     if s[i] == '+':
#         counter1 += 1
# print(f'Символ + встречается {counter1} раз')
# print(f'Символ * встречается {counter} раз')



# ''' ответ препода '''
#
# s = input()
# cnt_plus = 0
# cnt_mul = 0
#
# for el in s:
#     if el == "+":
#         cnt_plus += 1
#     elif el == "*":
#         cnt_mul += 1
#
# print("Символ + встречается", cnt_plus, "раз")
# print("Символ * встречается", cnt_mul, "раз")

# ''' или так '''
#
# n = input()
# print("Символ + встречается", n.count("+"), "раз")
# print("Символ * встречается", n.count("*"), "раз")


# ''' программа, которая определяет сколько в ней одинаковых соседних символов. '''
#
# s = input()
# counter = 0
# for i in range(len(s) - 1):
#     if s[i] == s[i + 1]:
#         counter += 1
# print(counter)


# s = input().lower()
# vowels = 'ауоыиэяюёе'
# consonants = 'бвгджзйклмнпрстфхцчшщ'
# counter = 0
# counter1 = 0
# for i in s:
#     if i in vowels:
#         counter += 1
# for j in s:
#     if j in consonants:
#         counter1 += 1
# print(f'Количество гласных букв равно {counter}')
# print(f'Количество согласных букв равно {counter1}')



# ''' программа, которая переводит данное число в двоичную систему счисления. '''
#
# n = int(input())
# a = format(n, 'b')
# print(a)
