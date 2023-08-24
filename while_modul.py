''' nachalo noviyi modul -- while '''


# ''' считывает числа и выводит их квадраты, пока не будет введено -1 '''
#
#
# num = int(input())
# while num != -1:
#     print('Квадрат вашего числа равен:', num * num)
#     num = int(input())



# Напишем программу, выводящую все числа, кратные 3, используя цикл for и while:
#
# # используем for
# for i in range(0, 100, 3):
#     print(i)
#
# # используем while
# i = 0
# while i < 100:
#     print(i)
#     i += 3

# ''' программa которая считывает числа и находит их сумму,
# до тех пор пока пользователь не введет слово stop:'''
#
# text = input()
# total = 0
# while text != 'stop':
#     num = int(text)
#     total += num
#     text = input()
# print('Сумма чисел равна', total)


# ''' вывести общее количество членов данной последовательности '''
#
# s = input()
# a = 0
# while s != 'стоп' and s != 'хватит' and s != 'достаточно':
#     a += 1
#     s = input()
# print(a)


# ''' программе подается последовательность целых чисел делящихся на 7 '''
#
# s = int(input())
#
# while s % 7 == 0:
#     print(s)
#     s = int(input())


# ''' Сумма чисел '''

# n = int(input())
# total = 0
# while n > 0:
#     total += n
#     print(n)
#     n = int(input())
# print(total)



# ''' программa, которая выводит количество пятерок. '''
#
# total = 0
# n = int(input())
# while 0 <= n <= 5:
#     if n == 5:
#         total += 1
#     print(n)
#     n = int(input())
# print(total)



# ''' программa, которая определяет, какое минимальное
# количество чеканных монет с номиналами 1, 5, 10, 25 '''
#
# n = int(input())
# counter = 0
# while n >= 25:
#     counter += 1
#     n = n - 25
# while n >= 10:
#     counter += 1
#     n = n - 10
# while n >= 5:
#     counter += 1
#     n = n - 5
# while n >= 1:
#     counter += 1
#     n = n - 1
# print(counter)


# ''' или так '''


# price = int(input())
# monety = 0
# while price > 0:
#     if price >= 25:  # пока цена больше 25
#         price -= 25  # отнимаем по 25
#
#     elif 10 <= price < 25:  # пока больше 10
#         price -= 10  # отнимаем по 10 и тд
#
#     elif 5 <= price < 10:
#         price -= 5
#
#     elif price < 5:
#         price -= 1
#
#     monety += 1  # считаем по монетке,
#
# print(monety)  # пока все не заплатят


# ''' или так '''


# n = int(input())
# k = 0
# for i in (25, 10, 5, 1):
#     while n // i > 0:
#         k += 1
#         n -= i
# print(k)


