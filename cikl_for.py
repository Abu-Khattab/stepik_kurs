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



#
# counter = 0
# for _ in range(10):
#     num = int(input())
#     if num > 10:
#         counter = counter + 1
# print('Было введено', counter, 'чисел, больших 10.')
#

#
# counter1 = 0
# counter2 = 0
# for _ in range(10):
#     num = int(input())
#     if num > 10:
#         counter1 = counter1 + 1
#     if num == 0:
#         counter2 = counter2 + 1
# print('Было введено', counter1, 'чисел, больших 10.')
# print('Было введено', counter2, 'нулей.' )
#

#
# counter = 0
# for i in range(1, 101):
#     if i**2 % 10 == 4:
#         counter = counter + 1
# print(counter)
#

#
# total = 0
# for _ in range(10):
#     num = int(input())
#     if num > 10:
#         total = total + num
# print('Сумма чисел больших 10 равна',  total)
#

#
# ''' число является простым, если оно не имеет делителей, кроме 1 и самого себя '''
#
# num = int(input())
# flag = True
#
# for i in range(2, num):
#     if num % i == 0:        #  если исходное число делится на какое-либо отличное от 1 и самого себя
#         flag = False
#
# if num == 1:
#     print('Это единица, она не простая и не составная')
# elif flag == True:
#     print('Число простое')
# else:
#     print('Число составное')
#

#
# largest = int(input())  # принимаем первое число за максимальное
# for _ in range(9):
#     num = int(input())
#     if num > largest:
#         largest = num
# print('Наибольшее число равно', largest)
#


# ''' сумма всех чисел двумя способами '''
#
# total = 0
# for i in range(1, 101):
#     total += i
# print(total)
#
#
#
# s = ((1 + 100) / 2) * 100  # формула Гаусса
# print(s)



# a, b = int(input()), int(input())
# counter = 0
# for i in range(a, b + 1):
#     if (counter ** 2) % 10 == 4 or (counter ** 2) % 10 == 9:
#         counter += i
# print(counter)


# ''' Количество чисел '''
#
# a, b = int(input()), int(input())
# counter = 0
# for i in range(a, b + 1):
#     if (i ** 3) % 10 == 4 or (i ** 3) % 10 == 9:
#         counter += 1
# print(counter)



# ''' подсчитывает сумму введенных чисел '''
#
#
# n = int(input())
# total = 0
# for i in range(n):
#     c = int(input())
#     total += c
# print(total)


# ''' вычисления натурального логарифма '''
#
#
# from math import *
#
# n = int(input())
# total = 0
# for i in range(1, n + 1):
#     total += 1 / i
# print(total - log(n))



# ''' подсчитывает сумму тех чисел от
# 1 до n (включительно), квадрат которых оканчивается на 5 '''
#
# n = int(input())
# total = 0
# for i in range(1, n + 1):
#     if (i ** 2) % 10 == 5:
#         total += i
# print(total)
#
#
# ''' или так '''
#
#
# n = int(input())
#
# sm = 0
# for i in range(1, n + 1):
#     square = i ** 2
#     if square % 10 == 2 or square % 10 == 5 or square % 10 == 8:
#         sm += i
#
# print(sm)


# ''' или так '''
#
#
# n, sum = int(input()), 0
# for i in range(1, n + 1):
#     if i**2 % 10 in [2, 5, 8]:
#         sum += i
# print(sum)


# ''' Факториал '''
#
# from math import *
#
# n = int(input())
# print(factorial(n))


# ''' считывает 10 чисел и выводит произведение отличных от нуля чисел '''
#
# total = 1
# for _ in range(10):
#     n = int(input())
#     if n > 0:
#         total *= n
# print(total)


# ''' вычисляет сумму всех его делителей '''

# n = int(input())
# total = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         total += i
# print(total)



# ''' вычисления знакочередующей суммы '''
#
# n = int(input())
# total = 0
# for i in range(n):
#     if i % 2 == 0:
#         total += i + 1
#     else:
#         total -= i + 1
# print(total)


# ''' Наибольшие числа 🌶️🌶️ '''

# n = int(input())
# max1 = 0
# max2 = 1
# for i in range(1, n + 1):
#     num = int(input())
#     if num > max1:
#         max2 = max1
#         max1 = num
#     elif num > max2:
#         max2 = num
# print(max1)
# print(max2)


# ''' Only even numbers 🌶️ '''
#
# events = 0
#
# for i in range(10):
#     s = int(input())
#     if s % 2 == 0:
#         events += 1
# if events == 10:
#     print("YES")
# else:
#     print("NO")
#
#
#
# ''' или так '''
#
# flag = True
# for _ in range(10):
#     n = int(input())
#
#     if n % 2 == 1:
#         flag = False
#
#
# if flag:
#     print('YES')
# else:
#     print('NO')


# ''' Последовательность Фибоначчи 🌶️ '''

# n = int(input())
# a = 1
# y = 0
# for i in range(n):
#     b = a
#     a = b + y
#     y = b
#     print(b, end=' ')


# ''' или так '''

# n = int(input())
# a, b = 1, 1
#
# for i in range(n):
#     print(a, end=' ')
#     a, b = b, a + b


