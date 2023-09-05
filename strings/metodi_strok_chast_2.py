''' начало подмодуля методы строк часть 2 '''

# ''' программа, которая подсчитывает количество слов '''
#
# s = input().split()
# print(len(s))
#
#
# text = input()  # Ввод строки текста
# word_count = text.count(' ') + 1  # Подсчет количества слов
# print(word_count)  # Вывод количества слов


# ''' программа, которая подсчитывает сколько
#  аденина, гуанина, цитозина и тимина входит в данную строку генетического кода '''

# s = input().upper()
# print("Аденин:", s.count('А'))
# print("Гуанин:", s.count('Г'))
# print("Цитозин:", s.count('Ц'))
# print("Тимин:", s.count('Т'))


# ''' или так '''

# s = input().upper()
# for c in ('Аденин:', 'Гуанин:', 'Цитозин:', 'Тимин:'):
#     print(c, s.count(c[0]))


# ''' количество строк в которых содержится число 11 минимум 3 раза '''
#
# n = int(input())
# result = []
# for i in range(n):
#     s = input()
#     total = s.count('11')
#     if total >= 3:
#         result.append(s)
# print(len(result))
#
#
# ''' или так '''
#
# n = int(input())
# cnt = 0
#
# for _ in range(n):
#     message = input()
#     if message.count("11") >= 3:
#         cnt += 1
#
# print(cnt)



# ''' подсчитывает количество цифр в данной строке '''
#
# s = input()
# counter = 0
# figure = '0123456789'
# for i in s:
#     if i in figure:
#         counter += 1
# print(counter)


# ''' или '''
#
# s = input()
# k = 0
# for c in '1234567890':
#   k += s.count(c)
# print(k)


# ''' «YES» если введенная строка заканчивается подстрокой .com или .ru
#     и «NO» в противном случае '''
#
# s = input()
# if s.endswith('com') or s.endswith('ru'):
#     print("YES")
# else:
#     print("NO")
#
# ''' или '''
#
# print('YES' if input().endswith(('.com','.ru')) else 'NO')


# '''  выводит символ, который появляется наиболее часто '''
#
# s = input()
# s = list(s)
# maxx = max(s, key=s.count)
# print(maxx)
#
#
# ''' Если таких символов несколько, следует вывести последний по порядку символ. '''
#
# s = input()
# most_common = s[0]
# for el in s:
#     if s.count(el) >= s.count(most_common):
#         most_common = el
#
# print(most_common)


# ''' Первое и последнее вхождение '''
#
# s = input()
# if s.count('f') == 1:
#     print(s.find('f'))
# if s.count('f') > 1:
#     print(s.find('f'), s.rfind('f'))
# if s.count('f') == 0:
#     print("NO")
#
#
# ''' или '''
#
# s = input()
# cnt = s.count("f")
#
# if cnt == 0:
#     print("NO")
# elif cnt == 1:
#     print(s.index("f"))
# else:
#     print(s.index("f"), s.rindex("f"))


# ''' Удаление фрагмента '''
#
# s = input()
# a = s[:s.find('h')]
# b = s[s.rfind('h') + 1:]
# print(a + b)