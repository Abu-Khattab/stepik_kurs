# ''' Список чисел '''
#
# n = int(input())
# numbers = list(range(1, n + 1))
# print(numbers)



# n = int(input())
# abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
#        'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# print(abc[:n])

# ''' или '''

# n = int(input())
# s = ''
# for i in range(n):
#     s += chr(ord("a") + i)
# print(list(s))


# ''' или '''
#
# n = int(input())
# s = ''
# for i in range(n):
#     s += chr(97 + i)
# print(list(s))


# ''' Замена элементов списка '''
#
# rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
#
# rainbow[3] ='Зеленый'
# rainbow[-1] ='Фиолетовый'
#
# print(rainbow)
#
# ''' или '''
#
# rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
# rainbow[3::3] = ['Зеленый', 'Фиолетовый']
# print(rainbow)
#
# ''' или '''
#
# rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
# rainbow[rainbow.index('Green')] = 'Зеленый'
# rainbow[rainbow.index('Violet')] = 'Фиолетовый'
# print(rainbow)


# ''' в обратном порядке '''
#
#
# languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
# print(languages[::-1])
#
#
# ''' или '''
#
# languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
# languages.reverse()
# print(languages)
