'''Sozdal novuyu vetku dlya praktiki'''



# a = 15 // (16 % 7)
# b = 34 % a * 5 - 29 % 5 * 2
# print(a + b)

''' геометрическая прогрессия'''

# b1, q, n = int(input()), int(input()), int(input())
# b = b1 * q ** (n - 1)
# print(b)

# u, m = int(input()), int(input())
#
# print(m // u)
# print(m % u)



''' Количество выживших'''

# n = int(input())
# print(((n % 2) + n) // 2)
#
#
# n = int(input())
# print((n + 1) // 2) # можно и так



''' номер купе '''

# n = int(input())
#
# print(-(-n // 4))


''' Пересчёт временного интервала'''

# n = int(input())
# s = n //  60
# m = n % 60
# print(n, "минут - это", s, "час", m, "минут." )


''' программа, в которой рассчитывается сумма и произведение цифр положительного трёхзначного числа.'''

# n = int(input())
# pc = n // 100
# sc = (n % 100) // 10
# poc = n % 10
# print("Сумма цифр =", pc + sc + poc)
# print("Произведение цифр =", pc * sc * poc)


''' программа, которая выводит шесть чисел, образованных при перестановке цифр заданного числа'''

# n = int(input())
# nc = n // 100
# sc = (n % 100) // 10
# ps = n % 10
# print(n)
# print(nc, ps, sc, sep='')
# print(sc, nc, ps, sep='')
# print(sc, ps, nc, sep='')
# print(ps, nc, sc, sep='')
# print(ps, sc, nc, sep='')


# number = int(input())
#
# d1 = (number // 10 ** 2) % 10
# d2 = (number // 10 ** 1) % 10  # можно и так
# d3 = (number // 10 ** 0) % 10
#
# print(d1, d2, d3, sep="")
# print(d1, d3, d2, sep="")
# print(d2, d1, d3, sep="")
# print(d2, d3, d1, sep="")
# print(d3, d1, d2, sep="")
# print(d3, d2, d1, sep="")

''' программа для нахождения цифр четырёхзначного числа'''

# n = int(input())
# nc = n // 1000
# vc = (n % 1000) // 100
# tc = (n % 100) // 10
# pc = n % 10
#
# print("Цифра в позиции тысяч равна", nc)
# print("Цифра в позиции сотен равна", vc)
# print("Цифра в позиции десятков равна", tc)
# print("Цифра в позиции единиц равна", pc)


# n = int(input())
#
# d1 = (n // 10 ** 3) % 10
# d2 = (n // 10 ** 2) % 10  # можно и так
# d3 = (n // 10 ** 1) % 10
# d4 = (n // 10 ** 0) % 10
#
# print("Цифра в позиции тысяч равна", d1)
# print("Цифра в позиции сотен равна", d2)
# print("Цифра в позиции десятков равна", d3)
# print("Цифра в позиции единиц равна", d4)


# n, s = int(input()), int(input())
# ks = (n + s)** 2
# sk = (n ** 2) + (s ** 2)
# print("Квадрат суммы", n, "и", s, "равен", ks)
# print("Сумма квадратов", n, "и", s, "равна", sk)


# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# print((a**b) + (c**d))


''' Программа должна вывести число n + nn + nnn '''

# n = int(input())
# print(n + (n * 11) + (n * 111))

