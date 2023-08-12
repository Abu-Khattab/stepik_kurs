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




# x = int(input())
# if 0 <= x <= 16:
#     print("Принадлежит")
# else:
#     print("Не принадлежит")


# x = int(input())
# if x <= - 3 or x >= 7:
#     print("Принадлежит")
# else:
#     print("Не принадлежит")


# x = int(input())
#
# if (- 30 < x <= -2) or (7 < x <= 25):
#     print("Принадлежит")
# else:
#     print("Не принадлежит")


# n = int(input())
#
# if 1000 <= n <= 9999:
#     if n % 7 == 0 or n % 17 == 0:
#         print("YES")
#     else:
#         print("NO")
# else:
#     print("NO")



# a, b, c = int(input()), int(input()), int(input())
#
# if (a + b) > c and (a + c) > b and (c + b) > a:
#     print("YES")
# else:
#     print("NO")


# ''' Високосный год '''
#
# n = int(input())
# if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
#     print("YES")
# else:
#     print("NO")


# a, b, c, d = int(input()), int(input()), int(input()), int(input())
#
# if a == c or b == d:
#     print("YES")
# else:
#     print("NO")



# a, b, c, d = int(input()), int(input()), int(input()), int(input())
#
# if abs(a - c) <= 1 and abs(b - d) <= 1:
#     print("YES")
# else:
#     print("NO")




# n, k = int(input()), int(input())
#
# if n < k:
#     print("YES")
# elif k < n:
#     print("NO")
# else:
#     print("Don't know")



# a, b, c = int(input()), int(input()), int(input())
#
# if a == b == c:
#     print("Равносторонний")
# elif a == b != c or a == c != b or c == b != a:
#     print("Равнобедренный")
# else:
#     print("Разносторонний")



# ''' среднее число '''
#
# a, b, c = int(input()), int(input()), int(input())
#
# if (a < b < c) or (c < b < a):
#     result = b
# elif (b < a < c) or (c < a < b):
#     result = a
# else:
#     result = c
# print(result)



# n = int(input())
# a = 1, 3, 5, 7, 8, 10, 12
# b = 4, 6, 9, 11
# c = 28
# if n in a:
#     print(31)
# elif n in b:
#     print(30)
# else:
#     print(c)



# weight = int(input())
# if weight < 60:
#     print("Легкий вес")
# elif 60 <= weight < 64:
#     print("Первый полусредний вес")
# else:
#     print("Полусредний вес")



# n, n1, s = int(input()), int(input()), input()
# s1 = '*', '+', '-', '/'
# if n1 == 0 and s == '/':
#     print("На ноль делить нельзя!")
# if s in s1:
#     if s == '*':
#         print(n * n1)
#     if s == '+':
#         print(n + n1)
#     if s == '-':
#         print(n - n1)
#     if s == '/' and n1 != 0:
#         print(n / n1)
# else:
#     print("Неверная операция")


# # Считываем названия двух основных цветов
# color1 = input("Введите название первого цвета: ")
# color2 = input("Введите название второго цвета: ")
#
# # Проверяем введенные значения
# if color1 == "красный" and color2 == "синий" or color1 == "синий" and color2 == "красный":
#     result = "фиолетовый"
# elif color1 == "красный" and color2 == "желтый" or color1 == "желтый" and color2 == "красный":
#     result = "оранжевый"
# elif color1 == "синий" and color2 == "желтый" or color1 == "желтый" and color2 == "синий":
#     result = "зеленый"
# elif color1 == "красный" and color2 == "красный":
#     result ="красный"
# elif color1 == "синий" and color2 == "синий":
#     result = "синий"
# elif color1 == "желтый" and color2 == "желтый":
#     result = "желтый"
# else:
#     result = "Ошибка! Введите названия 'красный', 'синий' или 'желтый'."
#
# # Выводим результат
# print(result)


# def mix_colors(color1, color2):
#     if color1 == 'красный' and color2 == 'синий' or color1 == 'синий' and color2 == 'красный':
#         return 'фиолетовый'
#     elif color1 == 'красный' and color2 == 'желтый' or color1 == 'желтый' and color2 == 'красный':
#         return 'оранжевый'
#     elif color1 == 'синий' and color2 == 'желтый' or color1 == 'желтый' and color2 == 'синий':
#         return 'зеленый'
#     elif color1 == 'красный' and color2 == 'красный':
#         return 'красный'
#     elif color1 == 'синий' and color2 == 'синий':
#         return 'синий'
#     elif color1 == 'желтый' and color2 == 'желтый':
#         return 'желтый'
#     else:
#         return 'Ошибка: неверное название цвета'
#
# # Считываем названия цветов от пользователя
# color1 = input('Введите первый цвет: ')
# color2 = input('Введите второй цвет: ')
#
# # Вызываем функцию для смешивания цветов и выводим результат
# result = mix_colors(color1, color2)
# print('Результат смешивания:', result)



# n = int(input())
# if n == 0:
#     print("зеленый")
# elif n >= 1 and n <= 10 and n % 2 != 0:
#     print("красный")
# elif n >= 1 and n <= 10 and n % 2 == 0:
#     print("черный")
# elif n >= 11 and n <= 18 and n % 2 != 0:
#     print("черный")
# elif n >= 11 and n <= 18 and n % 2 == 0:
#     print("красный")
# elif n >= 19 and n <= 28 and n % 2 != 0:
#     print("красный")
# elif n >= 19 and n <= 28 and n % 2 == 0:
#     print("черный")
# elif n >= 29 and n <= 36 and n % 2 != 0:
#     print("черный")
# elif n >= 29 and n <= 36 and n % 2 == 0:
#     print("красный")
# else:
#     print("ошибка ввода")

# ''' точки пересечения '''
# a1 = int(input("Введите левую границу первого отрезка: "))
# b1 = int(input("Введите правую границу первого отрезка: "))
# a2 = int(input("Введите левую границу второго отрезка: "))
# b2 = int(input("Введите правую границу второго отрезка: "))
#
# if b1 < a2 or b2 < a1:
#     print("Пустое множество")
# else:
#     left = max(a1, a2)
#     right = min(b1, b2)
#     if left == right:
#         print("Точка:", left)
#     else:
#         print("Отрезок: [", left, ";", right, "]")


# ''' или так '''

# a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
# if a1 < a2:
#     amax = a2
# else:
#     amax = a1
# if b1 < b2:
#     bmin = b1
# else:
#     bmin = b2
# if amax > bmin:
#     print('пустое множество')
# elif amax == bmin:
#     print(amax)
# else:
#     print(amax, bmin)