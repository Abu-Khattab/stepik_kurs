''' strokovii tip dannikh '''

# print('"Python is a great language!", said Fred.' + '"I' "don't " 'ever remember having this much fun before."')


# name, last_name = input(), input()
# print("Hello", name, last_name, "! You have just delved into Python")

# name = input()
# print("Футбольная команда ", name, "имеет длину", len(name), "символов")



# ''' Три города '''
#
#
# city1 = input("Введите название первого города: ")
# city2 = input("Введите название второго города: ")
# city3 = input("Введите название третьего города: ")
#
# length_city1 = len(city1)
# length_city2 = len(city2)
# length_city3 = len(city3)
#
# shortest_length = min(length_city1, length_city2, length_city3)
# longest_length = max(length_city1, length_city2, length_city3)
#
# shortest_city = ""
# longest_city = ""
#
# if length_city1 == shortest_length:
#     shortest_city = city1
# if length_city2 == shortest_length:
#     shortest_city = city2
# if length_city3 == shortest_length:
#     shortest_city = city3
#
# if length_city1 == longest_length:
#     longest_city = city1
# if length_city2 == longest_length:
#     longest_city = city2
# if length_city3 == longest_length:
#     longest_city = city3
#
# print("Самое короткое название города:", shortest_city)
# print("Самое длинное название города:", longest_city)


# ''' или так '''
#
# a, b, c = input(), input(), input()
#
# if len(a) < len(b):
#     b, a = a, b
#
# if len(b) < len(c):
#     c, b = b, c
#
# if len(a) < len(b):
#     b, a = a, b
#
# print(c, a, sep='\n')


# ''' или так '''

# a = input()
# b = input()
# c = input()
# if min (len(a), len(b), len(c)) == len(a):
#     print(a)
# elif min (len(a), len(b), len(c)) == len(b):
#     print(b)
# else:
#     print(c)
# if max (len(a), len(b), len(c)) == len(a):
#     print(a)
# elif max (len(a), len(b), len(c)) == len(b):
#     print(b)
# else:
#     print(c)


# ''' у функций мин и макс есть ключи '''

# a, b, c = str(input()), str(input()), str(input())
# print(min(a, b, c, key=len ))
# print(max(a, b, c, key=len ))



# ''' арифметическая прогресия '''
#
#
# a1, n, d = len(input()), len(input()), len(input())
# summ = a1 + n + d
# s_max = max(a1, n, d)
# s_min = min(a1, n, d)
# sred = summ - s_max - s_min
# if sred - s_min == s_max - sred:
#     print("YES")
# else:
#     print("NO")


# ''' или так '''
#
# a, b, c = len(input()), len(input()), len(input())
# if a + b + c == (min(a, b, c) + max(a, b, c))/2*3:
#     print("YES")
# else:
#     print("NO")


# ''' или так '''

# a = len(input())
# b = len(input())
# c = len(input())
# if ((a + b + c)%3) == 0:
#     print('YES')
# else:
#     print('NO')


# ''' найти подстроку '''


# s = input()
# if 'синий' in s:
#     print("YES")
# else:
#     print("NO")


# s = input()
# if 'суббота' in s or 'воскресенье' in s:
#     print("YES")
# else:
#     print("NO")


# s = input()
# if '@' in s and '.' in s:
#     print("YES")
# else:
#     print("NO")