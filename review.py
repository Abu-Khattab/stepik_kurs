''' Новый подмодуль - ревью кода '''

# count = 0
# total = 1
# for i in range(1, 11):
#     n = int(input())
#     if n >= 0:
#         total *= n
#         count += 1
# if count == 0:
#     print('NO')
# else:
#     print(count)
#     print(total)




# ''' Ревью кода-2 🌶️🌶️
#   программу, которая выводит на экран сумму всех отрицательных чисел последовательности
#   и максимальное отрицательное число в последовательности.
# '''
#
# mx = 0
# s = 0
# for i in range(10):
#     x = int(input())
#     if x < 0:
#         s += x
#         if mx == 0 or x > mx:
#             mx = x
# if s:
#     print(s)
#     print(mx)
# else:
#     print('NO')


# max_number = -10 ** 6
# total = 0
# for i in range(10):
#     n = int(input())
#     if n < 0:
#         total += n
#         if n > max_number:
#             max_number = n
# if total == 0:
#     print("NO")
# else:
#     print(total)
#     print(max_number)




# mx = -10**6 # неверно задана переменная (сравнивать будет с минимальным)
# s = 0
# for _ in range(10):  # неверно задан диапозон (было 11), замена "i" на "_"
#     x = int(input())
#     if x < 0:
#         s += x  # неверно задана формула (было равенство "=")
#         if x > mx:  # смещен блок кода, чтобы условие работало только для x < 0
#             mx = x
# if s == 0:  # не был задано условие для вывода при отсутствии отрицательных чисел
#     print('NO')
# else:
#     print(s)
#     print(mx)


# ''' Ревью кода-3
#   программа, которая подсчитывает и выводит
#   сумму всех чётных чисел последовательности
#  '''
#
# total = 0
# for _ in range(1, 8):
#     n = int(input())
#     if n % 2 == 0:
#         total += n
# if total <= 0:
#     print("0")
# else:
#     print(total)


# ''' Ревью кода-4 🌶️🌶️
#   программу, которая выводит на экран максимальную цифру числа, кратную 3
#  '''
#
# n = int(input())
# max_digit = -1  # Изменяем начальное значение на -1, чтобы корректно обрабатывать случай отсутствия цифр, кратных 3
#
# while n > 0:
#     digit = n % 10
#     if digit % 3 == 0:
#         if digit > max_digit:  # Исправляем условие на > вместо <
#             max_digit = digit
#     n = n // 10  # Исправляем нацелочисленное деление для обновления числа
#
# if max_digit == -1:  # Изменяем условие на -1, чтобы вывести 'NO' в случае отсутствия цифр, кратных 3
#     print('NO')
# else:
#     print(max_digit)


# ''' Ревью кода-5 🌶️
#     программу, которая выводит на экран его первую (старшую) цифру
# '''
#
# n = int(input())
# while n >= 10:
#     n //= 10
# print(n)



# ''' Ревью кода-6
#     программа, которая выводит на экран
#     произведение цифр введенного числа
# '''
#
# n = int(input())
# product = 1
# while n > 0:
#     digit = n % 10
#     product = product * digit
#     n //= 10
# print(product)