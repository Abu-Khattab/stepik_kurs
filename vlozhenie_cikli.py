''' Модуль по вложенным циклам '''



# ''' программу, которая печатает таблицу размером n×3 '''
#
# n = int(input())
# for i in range(n):
#     for j in range(1, 4):
#         print(n, end=' ')
#     print()


# ''' программу, которая печатает таблицу размером n×5,
#  где в i-ой строке указано число i '''
#
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, 6):
#         print(i, end=' ')
#     print()


# ''' программу, которая печатает таблицу сложения для всех чисел от 1 до n '''

# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, 10):
#         print(i, '+', j, '=', i + j)
#     print()


# ''' Звездный треугольник 🌶️🌶️ '''
#
# n = int(input())
# for i in range(1, n // 2 + 2):
#         print(i * '*')
# for j in range(n // 2, 0, -1):
#     print(j * '*')


# ''' Численный треугольник 1 '''
#
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(i):
#         print(i, end='')
#     print()


# ''' 12 месяцев '''

# for n in range(1, 13):
#     for k in range(1, 13):
#         for m in range(1, 12):
#             if 28*n + 30*k + 31*m == 365:
#                 print("n =", n, ", k =", k, ", m =", m)



# ''' Старинная задача '''

# total_money = 100
# total_heads = 100
#
# for bulls in range(total_heads + 1):
#     for cows in range(total_heads - bulls + 1):
#         calves = total_heads - bulls - cows
#         if (10 * bulls + 5 * cows + 0.5 * calves) == total_money:
#             print("Быки =", bulls, ", Коровы =", cows, ", Телята =", calves)



