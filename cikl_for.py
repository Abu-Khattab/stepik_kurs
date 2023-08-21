''' modul pro cikli '''

# s = 'Python is awesome!'
# for i in range(10):
#     print(s)


# s = input()
# s1 = int(input())
# for i in range(s1):
#     print(s)



# for i in range(6):
#     print('A' * 3)
# for i in range(5):
#     print('B' * 4)
# print('E')
# for i in range(9):
#     print('T' * 5)
# print('G')


# n = int(input())
# for i in range(n):
#     print('*' * 19)


# n = input()
# for i in range(10):
#     print(i, n)



# ''' Квадрат числа '''

# n = int(input())
# for i in range(n + 1):
#     print("Квадрат числа", i, "равен", i ** 2)



# ''' Звездный треугольник '''

# n = int(input())
# for i in range(n, 0, -1):
#     i = i * '*'
#     print(i)



# ''' Популяция '''
#
# m, p, n = float(input()), float(input()), int(input())
# for i in range(n):
#     s = m * (p / 100 + 1) ** i
#     print(i + 1, s)



# for i in range(5, 0, -1):
#     print(i, end=' ')
# print('Взлетаем!!!')



# n, m = int(input()), int(input())
# for i in range(n, m + 1):
#     print(i)




# ''' Последовательность чисел '''

# n, m = int(input()), int(input())
# if n < m:
#     for i in range(n, m + 1):
#         print(i)
# elif n > m:
#     for i in range(n, m - 1, -1):
#         print(i)
# else:
#     print(n)



# ''' выводит все нечетные числа от m до n включительно в порядке убывания. '''


# m, n = int(input()), int(input())
# for i in range(m, n - 1, -1):
#     if i % 2 != 0:
#         print(i)



# ''' выводит все числа от m до n включительно удовлетворяющие хотя бы одному из условий:
# число кратно 17;
# число оканчивается на 9;
# число кратно 3 и 5 одновременно. '''
#
#
# m, n = int(input()), int(input())
#
# for i in range(m, n):
#     if (i % 17 == 0) or (i % 10 == 9) or (i % 3 == 0 and i % 5 == 0):
#         print(i)


# ''' Таблица умножения '''


# n = int(input())
#
# for i in range(1, 11):
#         print(n, 'x', i, '=', n * i)