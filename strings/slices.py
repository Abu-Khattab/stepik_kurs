# # ''' СРЕЗЫ '''
#
#
# s = 'abcdefghij'
#
# print(s[2:5])
# print(s[0:6])
# print(s[2:7])
#
# print(s[2:])
# print(s[:7])
#
# print(s[-9:-4])
# print(s[-3:])
# print(s[:-3])
#
#
# ''' Шаг среза '''
#
# print(s[1:7:2])
#
#
#
# ''' Отрицательный шаг среза '''
#
#
# print(s[::-1])
#
# print(s[1:7:2])
# print(s[3::2])
# print(s[:7:3])
# print(s[::2])
# print(s[::-1])
# print(s[::-2])
#
# print(s[-2:]) # последние два символа строки
                # Если первый параметр среза больше второго, то срез создает пустую строку

# '''
#         5-го символа (не включительно) и с 6-го символа (включительно) по конец строки,
#         а между ними вставляем нужный нам символ, который встанет на
#         5-ю позицию (4 индекс)
# '''
#
# s = s[:4] + 'X' + s[5:]  # Мы создаем два среза: от начала строки до


# ''' программа, которая определяет является ли оно палиндромом. '''
#
# s = input()
# if s == s[::-1]:
#     print("YES")
# else:
#     print("NO")


# ''' или так '''
#
# word = input()
# flag_palindrom = True
# i = 0
# j = len(word) - 1
# while i < j:
#     if word[i] != word[j]:
#         flag_palindrom = False
#         break
#     i += 1
#     j -= 1
# if flag_palindrom:
#     print('YES')
# else:
#     print('NO')



# s = input()
#
# print(len(s))
# print(s * 3)
# print(s[0])
# print(s[:3])
# print(s[-3:])
# print(s[::-1])
# print(s[1:-1])


# ''' или так '''
#
# s = input()
# print(len(s), s * 3, s[0], s[0:3], s[-3:], s[::-1], s[1:-1], sep='\n')



# s = input()
#
# print(s[2])
# print(s[-2:-1])
# print(s[:5])
# print(s[:-2])
# for i in range(len(s)):
#     if i % 2 == 0:
#         print(s[i], end='')     # все символы с четными индексами;  n[::2]
# print()
# for i in range(len(s)):
#     if i % 2 != 0:
#         print(s[i], end='')     # все символы с нечетными индексами;  n[1::2]
# print()
# print(s[::-1])
# print(s[::-2])

# ''' или так '''
#
# n = input()
# print(n[2], n[-2], n[:5], n[0:-2], n[::2], n[1::2], n[::-1], n[::-2], sep='\n' )


# s = input()
#
# print(s[2])      # третий символ этой строки
# print(s[-2])     # предпоследний символ этой строки
# print(s[:5])     # первые пять символов этой строки
# print(s[:-2])    # всю строку, кроме последних двух символов
# print(s[::2])    # все символы с четными индексами
# print(s[1::2])   # все символы с нечетными индексами
# print(s[::-1])   # все символы в обратном порядке
# print(s[::-2])   # все символы строки через один в обратном порядке, начиная с последнего


# ''' программа, которая разрежет ее на две равные части,
#     переставит их местами и выведет на экран. '''
#
# def cut_and_swap(text):
#     length = len(text)
#     half_length = length // 2
#
#     first_half = text[:half_length + (length % 2)]
#     second_half = text[half_length + (length % 2):]
#
#     swapped_text = second_half + first_half
#
#     return swapped_text
#
#
# # Пример использования функции
# input_text = input("Введите строку текста: ")
# result = cut_and_swap(input_text)
# print("Результат:")
# print(result)
#
# ''' или так '''
#
# s = input()
# n = len(s)
#
# a = s[:(n + 1) // 2]
# b = s[(n + 1) // 2:]
#
# print(b + a)
#
# ''' или так '''
#
# s = input()
# x = len(s)
# a = x // 2 + x % 2
# print(s[a:] + s[:a])

