''' novyi modul chislovyie tipyi dannyikh '''

# ''' ploshad treugolnika'''

# n, r = float(input()), float(input())
#
# s = (1/2) * n * r
# print(s)


# ''' skorost babulek '''
#
# s, v1, v2 = float(input()), float(input()), float(input())
#
# t = s / (v1 + v2)
# print(t)


# ''' obratnoe chislo '''
#
# n = float(input())
# if n == 0:
#     print("Обратного числа не существует")
# else:
#     s = (n ** -1 )
#     print(s)


# ''' sobachie goda '''
#
# age = int(input())
# if age >= 2:
#     age = 21 + (age - 2) * 4
#     print(age)
# if age == 1 or age == 2:
#     age *= 10.5
#     print(age)


# ''' Дано положительное действительное число. Выведите его первую цифру после десятичной точки. '''
#
# number = float(input())
# n = (number - int(number)) * 10
# print(int(n))


# ''' Выведите его дробную часть '''

# number = float(input())
# n = (number - int(number)) % 10
# print(n)


# ''' или так '''
#
# number = float(input())
# print(number % 1)


# ''' находит наименьшее и наибольшее из пяти чисел '''
#
#
# a, b, c, d, f = int(input()), int(input()), int(input()), int(input()), int(input())
# print("Наименьшее число", min(a,b,c,d,f))
# print("Наибольшее число", max(a,b,c,d,f))


# ''' Сортировка трёх '''
#
# a, b, c = int(input()), int(input()), int(input())
# summ = a + b + c
# print(max(a, b, c))
# print(summ - max(a, b, c) - min(a, b, c))
# print(min(a, b, c))


# ''' srednee chislo '''
#
# n = int(input())
# a = n // 100
# b = (n % 100) // 10
# c = n % 10
# if c - a == b or a - c == b:
#     print("Число интересное")
# else:
#     print("Число неинтересное")


# ''' ili tak '''
#
# n = int(input())
#
# a = n // 100
# b = (n % 100) // 10
# c = n % 10
#
# a1 = max(a, b, c)
# b1 = min(a, b, c)
# k = a1 - b1
#
# summ = a + b + c
# k1 = summ - a1 - b1
#
# if k == k1:
#     print("Число интересное")
# else:
#     print("Число неинтересное")


# a1, a2, a3, a4, a5 = float(input()), float(input()), float(input()), float(input()), float(input())
# print(abs(a1) + abs(a2) + abs(a3) + abs(a4) + abs(a5))


# ''' Манхетнское расстояние '''
#
# p1, p2, q1, q2 = int(input()), int(input()), int(input()), int(input())
# distance = abs(p1 - q1) + abs(p2 - q2)
# print(distance)