
# a, b, c = 'Beegeek loves Stepik'.split()
# print(type(a))



# import matplotlib.pyplot as plt
# from matplotlib_venn import venn3
#
# venn3(subsets=(n, m, k, x, y, z), set_labels=("more", "derevnya", "gori"))
# plt.show()



# n, m, k, x, y, z = int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
#
# s = (n-x) + m + (k-y) + z
# print(s)




# ''' Книги на прочтение 🌶️ '''


# n, m, k, x, y, z, t, a = (int(input()) for _ in range(8))
#
# s1 = n + m - x - t
# s2 = m + k - y - t
# s3 = n + k - z - t
#
# s = (n - s1 - s3 - t) + (m - s1 - s2 - t) + (k - s2 - s3 - t)
#
# print(s)
# print(s1 + s2 + s3)
# print(a - s - s1 - s2 - s3 - t)



# ''' or '''
#
#
# n, m, k, x, y, z, t, a = (int(input()) for _ in range(8))
#
# i = n + m + k
# j = x + y + z
#
# print(3 * (t - i) + 2 * j)
# print(2 * i - j - 3 * t)
# print(a + i - j - t)





# numbers = {20, 6, 8, 18, 18, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 12, 8, 8, 10, 4, 2, 2, 2, 16, 20}
# average = sum(numbers) / len(numbers)
#
# print(average)



# numbers = {0, 1, 1, 2, 3, 3, 3, 5, 6, 7, 7}
#
# print(*numbers, sep='\n')



# myset1 = set([1, 2, 3, 4, 5])
# myset2 = set('12345')
#
# print(myset1 == myset2)
# print(myset1)
# print(myset2)


# ''' сумму квадротов элементов '''
#
# numbers = {9089, -67, -32, 1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111, 111, 1, 23}
# el = []
# for i in numbers:
#     el.append(i * i)
#     s = sum(el)
# print(s)
#
# ''' or '''
#
# numbers = {9089, -67, -32, 1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111, 111, 1, 23}
# print(sum(i**2 for i in numbers))
#
# ''' or '''
#
# numbers = {9089, -67, -32, 1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111, 111, 1, 23}
# print(sum([i*i for i in numbers]))



# fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
# fruits = sorted(fruits, reverse = True)
#
# print(*fruits, sep='\n')




# ''' проверить строку на уникальность элементов '''

# s = input()
# if len(set(s)) == len(s):
#     print('YES')
# else:
#     print('NO')

# ''' or '''

# s = input()
# result = ['YES' if len(set(s)) == len(s) else 'NO']
# print(*result)



# ''' or '''
#
# print('YES' if len(s := input()) == len(set(s)) else 'NO')


# ''' or '''
#
# a = input()
# print(('NO','YES')[len(a) == len(set(a))])




# a, b = input(), input()
#
# a1 = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
# result = set(a).union(set(b))
# if result == a1:
#     print('YES')
# else:
#     print('NO')



# ''' or '''
#
# # Ввод двух строк состоящих из цифр
# string1 = input()
# string2 = input()
#
# # Объединяем символы из обеих строк
# combined_string = string1 + string2
#
# # Преобразуем объединенную строку в множество символов
# combined_set = set(combined_string)
#
# # Создаем множество, содержащее все десять цифр
# all_digits = set("0123456789")
#
# # Проверяем, содержит ли множество combined_set все десять цифр
# if combined_set == all_digits:
#     print("Да, в обеих строках вместе используются все десять цифр.")
# else:
#     print("Нет, не во всех строках вместе используются все десять цифры.")


# ''' or '''
#
# print(('NO', 'YES')[len(set(input() + input())) == 10])


#
# ''' or '''
#
# numbers = set(input() + input())
# print('YES' if len(numbers) == 10 else 'NO')


# '''  '''

# a, b = input(), input()
# if set(a) == set(b):
#     print('YES')
# else:
#     print('NO')


# ''' or '''
# print(('NO', 'YES')[set(input()) == set(input())])


# ''' or '''
# print('YES' if set(input()) == set(input()) else 'NO')



# ''' для записи всех трех слов был использован один и тот же набор букв '''

# s = input().split()
# a = s[0]; b = s[1]; c = s[2]
# if set(a) == set(b) and set(c) == set(a):
#     print('YES')
# else:
#     print('NO')


# ''' or '''
# a, b, c = input().split()
# print(['NO', "YES"][set(a) == set(b) == set(c)])


# ''' or '''
# a, b, c = [set(i) for i in input().split()]
# print(['NO', 'YES'][a == b == c])




# myset = set()
# for i in range(10):
#     if i % 2 == 0:
#         myset.add('even')
#     else:
#         myset.add('odd')
# print(myset)


# for i in range(int(input())):
#     print(len(set(input().lower())))





# ''' для вывода общего количества уникальных символов во всех считанных словах без учета регистра '''


# my_set = set()
# for i in range(int(input())):
#     my_set.update(input().lower())
# print(len(my_set))


# ''' or '''
#
# print(len(set(''.join([input().lower() for _ in range(int(input()))]))))
#
#
#
# ''' or '''
#
# s = set()
# for i in range(int(input())):
#     s |= set(input().lower())
# print(len(s))




# '''  определения общего количества различных слов в строке текста '''

# import re
#
# text = input()
# # Удаляем лишние пробелы и преобразуем в нижний регистр (если нужно)
# cleaned_text = ' '.join(text.split()).lower()
#
# # Используем регулярное выражение для извлечения уникальных слов
# unique_words = set(re.findall(r'\b\w+\b', cleaned_text))
#
# # Выводим уникальные слова
# print("Уникальные слова в тексте:", len(unique_words))


# ''' or '''
#
# words = [word.lower().strip('.,;:-?!') for word in input().split()]
#
# print(len(set(words)))



# ''' or'''
#
# print(len(set(x.strip('.,;:-?!') for x in input().lower().split())))



# ''' or'''
#
# s = input().lower()
# n = ''
#
# for b in s:
#     if b not in ['.',',',';',':','-','?','!']:
#         n += b
#
# n = n.split()
# print(len(set(n)))



# ''' or '''
#
# s = input().lower()
# for ch in '.,;:-?!':
#     s = s.replace(ch, '')
# print(len(set(s.split())))



# ''' Встречалось ли число раньше? '''
#
# numbers = input().split()
# seen_numbers = set()
#
# for number in numbers:
#     if number in seen_numbers:
#         print("YES")
#     else:
#         seen_numbers.add(number)
#         print("NO")
#
#
# ''' or '''
#
# lst = [int(el) for el in input().split()]
# for i in range(len(lst)):
#     if lst[i] in lst[:i]:
#         print('YES')
#     else:
#         print('NO')



# X = int(input())
# hours = X // 60  # Целочисленное деление на 60 дает количество часов
# minutes = X % 60  # Остаток от деления на 60 дает количество минут
#
# # Выводим результат в формате HH:MM
# print(hours, minutes)



# ''' определяет количество чисел, которые есть как в первой строке, так и во второй.
#
# '''
#
# a = set(input().split())
# b = set(input().split())
# count = a & b
# print(len(count))
#
#
#
# ''' or '''
#
# print(len(set(input().split()) & set(input().split())))




# ''' выводит все числа в порядке возрастания, которые есть как в первой строке, так и во второй. '''
#
# a, b = set(input().split()), set(input().split())
# print(*sorted(a & b, key=int))
#
#
# ''' or '''
#
# set1 = set(int(i) for i in input().split())
# set2 = set(int(i) for i in input().split())
#
# print(*sorted(set1 & set2))
#
#
# ''' or '''
#
# print(*sorted(set(input().split()) & set(input().split()), key=int))
#
#
#
# ''' числа в порядке возрастания, которые есть в первой строке, но отсутствуют во второй.
#
#  '''
#
# set1 = set(int(i) for i in input().split())
# set2 = set(int(i) for i in input().split())
#
# print(*sorted(set1 - set2))



# ''' выводит все общие цифры в порядке возрастания у всех введенных чисел '''
#
# n = int(input())
# a = set(input())
# for i in range(n - 1):
#     b = set(input())
#     a = a.intersection(b)  # Пересекаем текущее множество с предыдущим
# result = sorted(a)  # Сортируем итоговое множество
# print(*result)





# ''' or '''
#
# n = int(input())
# numbers = [input() for _ in range(n)]
#
# num_set = set(numbers[0]).intersection(*numbers)
# print(*sorted(num_set))


# ''' or '''
#
# n, my_set = int(input()), set(input())
#
# for _ in range(n - 1):
#     my_set = my_set & set(input())
#
# print(*sorted(my_set, key=int))


# ''' Одинаковые цифры '''

# a, b = set(input()), set(input())
# if a.isdisjoint(b):
#     print('NO')
# else:
#     print('YES')


# ''' or '''
#
# print(("YES", "NO")[set(input()).isdisjoint(input())])



# ''' or '''
#
# print('NO' if set(input()).isdisjoint(set(input())) else 'YES')



# ''' входят ли в запись первого числа все цифры, содержащиеся в записи второго '''

# print('NO' if set(input()) <= (set(input())) else 'YES')




# ''' выводит множество оценок, которые есть и у первого и у второго
#  учеников, но которых нет у третьего ученика. '''
#
#
# a, b, c = [{*map(int, input().split())} for _ in range(3)]
# result = a & b
# res = result - c
# print(*sorted(res, reverse=True, key=int))
#
#
#
# ''' or '''
#
# set1 = set(int(i) for i in input().split())
# set2 = set(int(i) for i in input().split())
# set3 = set(int(i) for i in input().split())
#
# print(*sorted(set1 & set2 - set3, reverse=True))
#
#
# ''' or '''
#
# a, b, c = [set(map(int, input().split())) for _ in range(3)]
#
# print(*sorted((a & b) - c, reverse=True))


# ''' выводит такие оценки, которые встречаются не более, чем у двух учеников '''
#
# a, b, c = [set(map(int, input().split())) for _ in range(3)]
# res = a.intersection(b, c)
# result = (a | b | c) - res
# print(*sorted(result))


# ''' or '''
#
# a, b, c = [set(map(int, input().split())) for _ in range(3)]
#
# print(*sorted((a | b | c) - (a & b & c)))


# ''' выводит множество оценок третьего ученика, которые не встречаются ни у первого, ни у второго ученика. '''
#
# a, b, c = [set(map(int, input().split())) for _ in range(3)]
# print(*sorted(c - (a | b), reverse=True))


# ''' выводит множество оценок, не встречающихся ни у одного из трех учеников. '''

# a, b, c = [set(map(int, input().split())) for _ in range(3)]
# n = set(range(11))
# print(*sorted(n - (a | b | c)))


# ''' генераторы '''
#
# items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
# my_set = {int(el) for el in items}
# print(*sorted(my_set))
#
#
# ''' or '''
#
# items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
# print(*sorted(set(map(int, items))))



# ''' получить множество, содержащее первую букву каждого слова (в нижнем регистре) '''
#
# words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime',
#          'Lemon', 'grapes', 'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']
# print(*sorted({i[0].lower() for i in words}))





# import string
#
# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and,
# save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory,
#  over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely,
#   you all know those redolent remnants of day suspended, with the midges,
#   about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk;
#    a furry warmth, golden midges.'''
#
# # Очистим текст от знаков препинания
# translator = str.maketrans('', '', string.punctuation)
# cleaned_sentence = sentence.translate(translator)
#
# my_set = {word.lower() for word in cleaned_sentence.split()}
# print(*sorted(my_set))



# ''' or '''
#
# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and,
# save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory,
#  over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely,
#  you all know those redolent remnants of day suspended, with the midges,
#   about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk;
#    a furry warmth, golden midges.'''
#
# a = {i.strip(':,.!?();').lower() for i in sentence.split()}
# print(*sorted(a))



# ''' получить множество, содержащее уникальные слова  строки sentence длиною меньше 4 символов '''
#
# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and,
# save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory,
#  over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely,
#   you all know those redolent remnants of day suspended, with the midges,
#   about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk;
#    a furry warmth, golden midges.'''
#
# s = {i.strip(':,.!?();').lower() for i in sentence.split() if len(i.strip(':,.!?();')) < 4}
# print(*sorted(s))




# ''' Уникальные имена файлов c расширением .png '''
#
# files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT',
#          'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py',
#          'stepik.org', 'kotlin.ko', 'github.git']
#
# result = {file.lower() for file in files if file.lower().endswith('.png')}
# print(*sorted(result))


