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


# ''' считывает натуральное число (целое положительное) и обрабатывает его цифры '''
#
# n = int(input())
# while n != 0:  # пока в числе есть цифры
#     last_digit = n % 10  # получить последнюю цифру
#     # код обработки последней цифры
#     n = n // 10  # удалить последнюю цифру из числа



# ''' програмa, которая определяет есть ли в числе цифра 7 '''
#
# num = int(input())
# has_seven = False  # сигнальная метка
#
# while num != 0:
#     last_digit = num % 10
#     if last_digit == 7:
#         has_seven = True
#     num = num // 10
#
# if has_seven == True:
#     print('YES')
# else:
#     print('NO')


# ''' программa, которая выводит его цифры в столбик в обратном порядке '''
#
# n = int(input())
#
# while n != 0:
#     last_digit = n % 10
#     n = n // 10
#     print(last_digit)



# ''' программа, которая меняет порядок цифр числа на обратный '''
#
# n = int(input())
# while n > 0:
#     print(n % 10, end='')
#     n //= 10



# ''' max и min '''
#
# n = int(input())
# res = [int(x) for x in str(n)]
# print("Максимальная цифра равна", max(res))
# print("Минимальная цифра равна", min(res))


# '''
#  программа, которая вычисляет:
# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.
# '''

# n = int(input())
# res = [int(x) for x in str(n)]
# summ = sum(res)
# print(summ)
# dlina_res = len(res)
# print(dlina_res)
# proiz = 1
# for i in res:
#     proiz *= i
# print(proiz)
# sred_arif = summ / dlina_res
# print(sred_arif)
# if dlina_res == 3:
#     print(n // 100)
#     print((n // 100) + (n % 10))
# if dlina_res > 3:
#     print(n // 1000)
#     print((n // 1000) + (n % 10))
# if dlina_res <= 2:
#     print(n // 10)
#     print((n // 10) + (n % 10))


# ''' ili tak '''


# n = int(input())  # препарируемое число)))
# num = n  # уменьшаемый остаток для получения "стоп" в цикле
# total = 0  # сумма чисел
# product = 1  # произведение чисел
# quantity = 0  # количество чисел
#
#
# while num:
#     total += num % 10  # считаем суму чисел
#     product *= num % 10  # считаем произведение чисел
#     quantity += 1  # считаем количество чисел
#     num //= 10  # откидывает последнее число
#
# # выводим ответы
# print(total)  # сумма чисел
# print(quantity)  # количество чисел
# print(product)  # произведение чисел
# print(total / quantity)  # среднее арифмитическое всех чисел
# print(n // 10 ** (quantity - 1))  # первое число
# print(n // 10 ** (quantity - 1) + n % 10)  # произведение первого и последнего чисел



# ''' Вторая цифра '''

# n = int(input())
# s = [x for x in str(n)]
# print(s[1])

# ''' ili tak '''
#
# n = int(input())
# while n > 99:
#     n //= 10
# print(n % 10)



# ''' программа, которая определяет, состоит ли указанное число из одинаковых цифр '''
#
# n = int(input())
# s = [x for x in str(n)]
# if min(s) == max(s):
#     print("YES")
# else:
#     print("NO")
#
#
# ''' или так '''
#
# n = int(input())
# min_digit = 9
# max_digit = 0
#
# while n > 0:
#     last_digit = n % 10
#
#     min_digit = min(min_digit, last_digit)
#     max_digit = max(max_digit, last_digit)
#
#     n //= 10
#
# if min_digit == max_digit:
#     print("YES")
# else:
#     print("NO")


# ''' Упорядоченные цифры 🌶️ '''
#
#
# n = int(input())
# flag = True
# last_digit = n % 10
#
# while n > 0:
#     if last_digit > n % 10:
#         flag = False
#
#     last_digit = n % 10
#     n //= 10
#
# if flag:
#     print("YES")
# else:
#     print("NO")


# ''' программа, которая выводит его наименьший отличный от 1 делитель '''
#
# num = int(input())
# flag = True
#
# for i in range(2, num + 1):
#     if num % i == 0:
#         flag = False
#         print(i)
#         break


# ''' или так '''
#
# n = int(input())
#
# for i in range(2, n + 1):
#     if n % i == 0:
#         print(i)
#         break



# '''
# программу, которая выводит числа от
# 1 до n включительно за исключением:
# чисел от 5 до 9 включительно;
# чисел от 17 до 37 включительно;
# чисел от 78 до 87 включительно.
# '''

# def print_numbers(n):
#     for i in range(1, n + 1):
#         if (5 <= i <= 9) or (17 <= i <= 37) or (78 <= i <= 87):
#             continue
#         print(i)
#
# # Пример использования
# n = int(input("Введите число n: "))
# print_numbers(n)
#
#
# ''' или так '''
#
# n = int(input())
# for i in range(1, n + 1):
#     if (5 <= i <= 9) or (17 <= i <= 37) or (78 <= i <= 87):
#         continue
#     print(i)



