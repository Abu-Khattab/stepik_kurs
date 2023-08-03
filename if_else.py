''' Razdel uslovnyie operatoryi - if, else '''

# ''' программа, которая определяет, состоит ли двузначное число, введенное с клавиатуры, из одинаковых цифр'''

# num = int(input())
# last_digit = num % 10    # последняя цифра числа
# first_digit = num // 10  # первая цифра числа
#
# if last_digit == first_digit:
#     print('ДА')
# else:
#     print('НЕТ')


# ''' программа, которая считывает три числа и подсчитывает количество чётных чисел'''

# num1, num2, num3 = int(input()), int(input()), int(input())
# counter = 0  # переменная счётчик
# if num1 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
# if num2 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
# if num3 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
# print(counter)



# ''' Работа каких фрагментов кода правильно определяет, чётное или нет число содержится в переменной i ?'''
#
# i = int(input())
#
# if i / 2:
#     print(i, 'чётное')
# else:
#     print(i, 'нечётное')
# if i // 2:
#     print(i, 'чётное')
# else:
#     print(i, 'нечётное')
# if i % 2 == 0:
#     print(i, 'чётное')
# else:
#     print(i, 'нечётное')
# if i // 2 == 0:
#     print(i, 'чётное')
# else:
#     print(i, 'нечётное')
# if i % 2 != 0:
#     print(i, 'нечётное')
# else:
#     print(i, 'чётное')
# if i // 2 != 0:
#     print(i, 'нечётное')
# else:
#     print(i, 'чётное')


# ''' Корректный пароль '''
#
# s = input()
# s1 = input()
# if s == s1:
#     print("Пароль принят")
# else:
#     print("Пароль не принят")

# ''' определяет, является число четным или нечетным '''
#
# s = int(input())
# if s % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")


# ''' сумма первой и последней цифр равна разности второй и третьей цифр '''
#
# n = int(input())
#
# p = (n // 10 ** 3) % 10
# p1 = (n // 10 ** 2) % 10
# p2 = (n // 10 ** 1) % 10
# p3 = (n // 10 ** 0) % 10
#
# if p + p3 == p1 - p2:
#     print("ДА")
# else:
#     print("НЕТ")


# ''' if '''

# n = int(input())
#
# if n < 18:
#     print("Доступ запрещен")
# else:
#     print("Доступ разрешен")



# ''' Являеться ли геометрической прогрессией'''


# b1, q, n = int(input()), int(input()), int(input())
#
# if q - b1 == n - q:
#     print("Да")
# else:
#     print("Нет")



# ''' Наименьшее число'''
#
# n, n1 = int(input()), int(input())
# if n > n1:
#     print(n1)
# elif n < n1:
#     print(n)


# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# ab = 0
# cd = 0
#
# if a > b:
#     ab = b
# else:
#     ab = a
# if c > d:
#     cd = d
# else:
#     cd = c
# if ab < cd:
#     print(ab)
# else:
#     print(cd)


# ago = int(input())
# if ago <= 13:
#     print("детство")
# elif 14 <= ago <= 24:
#     print("молодость")
# elif 25 <= ago <= 59:
#     print("зрелость")
# else:
#     print("старость")




#''' сумма положительных чисел '''

# num1, num2, num3 = int(input()), int(input()), int(input())
#
# sum_of_positives = 0
#
# if num1 > 0:
#     sum_of_positives += num1
#
# if num2 > 0:
#     sum_of_positives += num2
#
# if num3 > 0:
#     sum_of_positives += num3
#
# print(sum_of_positives)
