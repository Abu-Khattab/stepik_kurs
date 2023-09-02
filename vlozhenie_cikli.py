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



# ''' программу, которая печатает численный треугольник с высотой равной n '''
#
# n = int(input())
# num = 0
# for row in range(1, n + 1):
#     for j in range(1, row + 1):
#         num += 1
#         print(num, end=' ')
#     print()

# ''' программу, которая печатает численный треугольник с высотой равной n '''

# n = int(input())
# for row in range(1, n + 1):
#     for i in range(row):
#         print(i + 1, end='')
#     for j in range(row - 1, 0, -1):
#         print(j, end='')
#     print()


# ''' число с максимальной суммой делителей и сумму его делителей. '''
#
# a = int(input())
# b = int(input())
# summ_count = 0
# max_i = 0
# for i in range(a, b + 1):
#     count = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             count += j
#         if count >= summ_count:
#             summ_count = count
#             max_i = i
# print(max_i, summ_count)



# ''' каждой строке напечатать очередное число и столько символов «+»,
#  сколько делителей у этого числа '''
#
# n = int(input())
# for i in range(1, n + 1):          # циклом перебираем все числа от 1 до n включительно
#     count = 0                      # вводим счетчик, который будет обнуляться каждую новую итерацию
#     for j in range(1, i + 1):      # во внутреннем цикле проверяем каждое из чисел на кол-во делителей
#         if i % j == 0:             # если делитель есть, то ->
#             count += 1             # -> к счетчику добавляем 1, это наши будующие плюсики
#     print(i, '+' * count, sep='')  # вывододим строку с числом и нужным кол-вом плюсов в рамках одной итерации


# ''' Цифровой корень '''
#
# n = int(input())
# while n > 9:
#     summ = 0
#     while n > 0:
#         last_digit = n % 10
#         summ += last_digit
#         n //= 10
#     n = summ
# print(n)



# ''' Сумма факториалов '''


# from math import *
#
# n = int(input())
# summ = 0
# for i in range(1, n + 1):
#     summ += factorial(i)
# print(summ)

# ''' или такие варианты '''

# 1 ВАРИАНТ
# from math import factorial
# n, total = int(input()), 0
# for i in range(1, n + 1):
#     total += factorial(i)
# print(total)

# 2 ВАРИАНТ
# n, total, multip = int(input()), 0, 1
# for i in range(1, n + 1):
#     multip *= i
#     total += multip
# print(total)

# 3 ВАРИАНТ
# n, total = int(input()), 0
# for i in range(1, n + 1):
#     multip = 1
#     for j in range(1, i + 1):
#         multip *= j
#     total += multip
# print(total)

# 4 ВАРИАНТ
# n = int(input())
# total = n
# while n > 1:
#     n -= 1
#     total = (total + 1) * n
# print(total)

# 5 ВАРИАНТ
# n, total = int(input()), 0
# for i in range(1, n + 1):
#     multip = 1
#     while i:
#         multip *= i
#         i -= 1
#     total += multip
# print(total)


# ''' программу, которая находит все простые числа от a до b включительно. '''

# a, b = int(input()), int(input())
#
# for i in range(a, b + 1):
#     count = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             count += 1
#     if count == 2:
#         print(i)
#
# ''' или так '''
# """Простое число делится только на 1 и само на себя. Решаем через счетчик
# делителей, или можно модифицировать код из 7.9.3. Для оптимизации кода я
# использую тот факт, что все делители кроме самого числа находятся в первой
# половине этого числа. И в этом случае у него может быть только один делитель
# (равный 1). Также, т.к. 1 не является простым числом, то есть 2 выхода:
# 1. Просто меняем его на 2, и учитываем это перед внешним циклом (на общий
# результат это не повлияет),
# 2. Или пропускаем этот вариант во внешнем цикле (через continue). Данный
# вариант предпочтительнее.
# """
#
# a, b = int(input()), int(input())
# for i in range(a, b + 1):
#     if i == 1:
#         continue                        # Учитываем, что 1 не является простым числом
#     count = 0                           # Задаем счетчик делителей. Тут же он обнуляется перед итерацией
#     for j in range(1, int(i / 2) + 1):  # Все делители числа i находятся в этом диапазоне (кроме него самого)
#         if i % j == 0:                  # Условие делителя
#             count += 1
#     if count == 1:                      # Условие для простого числа с учетом диапазона по j
#         print(i)



# total = 0
#
# for x in range(1, 777):
#     for y in range(1, 777):
#         if 12 * x + 13 * y == 777:
#             total += 1
#
# print('x =', x, 'y =', y)
# print('Общее количество натуральных решений =', total)


