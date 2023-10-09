# info = dict(name='Timur', age=28, job='Teacher')
# print(info)


# info_tuple = (['name', 'Timur'], ['age', 28], ['job', 'Teacher'])  # кортеж списков
# print(dict(info_tuple))  # создаем словарь на основе кортежа списков


# dict1 = dict.fromkeys(['name', 'age', 'job'], 'Missed information')
# print(dict1)


# dict1 = {}
# dict2 = dict()
#
#
# print(dict1)
# print(dict2)
# print(type(dict1))
# print(type(dict2))


# languages = {'Python': 'Гвидо ван Россум',
#              'C#': 'Андерс Хейлсберг',
#              'Java': 'Джеймс Гослинг'}
#
# info = dict(name='Timur', age=28, level='sinor', language='python', job='Teacher')
#
# print(languages)
# print(info)


# info = {'name': 'Timur',
#         'age': 28,
#         'job': 'Teacher',
#         'city': 'Moscow',
#         'email': 'timyr-guev@yandex.ru'}
#
# print(info['name'])
# print(info['email'])
# print(info['city'])


# ''' словарь на основании двух списков (кортежей) '''

# keys = ['name', 'age', 'job', 'city', 'email']
# values = ['Timur', 28, 'Teacher', 'Moscow', 'tima.email.ru']
#
# info = dict(zip(keys, values))
#
# print(info)


# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
#
# if 'Франция' in capitals:
#     print('Столица Франции - это', capitals['Франция'])
#     print(capitals)


# my_dict = {10: 'Россия', 20: 'США', 30: 'Франция'}
#
# print('Сумма всех ключей словаря =', sum(my_dict))


# capitals = {'Австралия': 'Сидней', 'Таджикистан': 'Душанбе', 'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
# months = {1: 'Январь', 2: 'Февраль', 3: 'Март'}
#
# print('Минимальный ключ =', min(capitals))
# print('Максимальный ключ =', max(months))


# my_dict = {1.12: 'aa', 67.9: 45, 3.11: 'ccc', 7.9: 'dd', 9.2: 'ee', 7.1: 'ff', 0.12: 'qq', 1.91: 'aa', 10.12: [1,
# 2, 3], 99.0: {9, 0, 1}}
# print(min(my_dict) + max(my_dict))


# capitals = {'Австралия': 'Сидней', 'Таджикистан': 'Душанбе', 'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
#
# for key in capitals:
#     print(key)
#
# print('--------------------------------')
#
# for key in capitals:
#     print(capitals[key])
#
#
# print('--------------------------------')
#
# for key in capitals:
#     print('Столица', key, '- это', capitals[key])
#
# print('--------------------------------')
#
#
# for key in capitals.keys():     # итерируем по списку ['Россия', 'Франция', 'Чехия']
#     print(key)
#
# print('--------------------------------')
#
#
#
# for value in capitals.values():     # итерируем по списку ['Москва', 'Париж', 'Прага']
#     print(value)
#
#
# print('--------------------------------')
#
#
# for item in capitals.items():
#     print(item)
#
#
# print('--------------------------------')
#
#
# for key, value in capitals.items():
#     print(key, '-', value)
#
#
# print('--------------------------------')
#
#
# print(*capitals, sep='\n')
#
#
# print('--------------------------------')


# capitals = {'Россия': 'Москва', 'Англия': 'Лондон', 'Чехия': 'Прага', 'Бразилия': 'Бразилиа'}
#
# for key in sorted(capitals):  # будет гарантированно выводить ключи словаря в алфавитном порядке, по возрастанию:
#     print(key)
#
# print('-----------------------------------')
#
# for key, value in sorted(capitals.items(), key=lambda x: x[1]):
#     print(value)                # будет гарантированно выводить значения словаря в алфавитном порядке, по возрастанию:


# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
#
# if 'Россия' in capitals:        # Проверка наличия ключа в словаре:
#     print('В словаре есть ключ Россия')
#
#
# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
#
# if 'Париж' in capitals.values():            # Проверка наличия значения в словаре:
#     print('В словаре есть значение Париж')


# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
#
# res = [i['name'] for i in users if i['phone'][-1] == '8']   # res = [user['name'] for user in users if user['phone'].endswith('8')]
# print(*sorted(res))


# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
#
# res = [user['name'] for user in users if 'email' not in user.keys() or user['email'] == '']
# print(*sorted(res))





# my_dict = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
# n = input()
# result = ' '.join([my_dict[digit] for digit in n])
# print(result)






# digits = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
#           '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
#
# print(*[digits[c] for c in input()])






# my_dict = {'CS101': '3004, Хайнс, 8:00',
#            'CS102': '4501, Альварадо, 9:00',
#            'CS103': '6755, Рич, 10:00',
#            'NT110': '1244, Берк, 11:00',
#            'CM241': '1411, Ли, 13:00'}
# n = input()
# print(f'{n}: {my_dict[n]}')



# ''' nokia 3310 '''
#
#
# # Создаем словарь для сопоставления букв и нажатий клавиш
# letter_to_keypress = {
#     '.': '1', ',': '11', '?': '111', '!': '1111', ':': '11111',
#     'A': '2', 'B': '22', 'C': '222',
#     'D': '3', 'E': '33', 'F': '333',
#     'G': '4', 'H': '44', 'I': '444',
#     'J': '5', 'K': '55', 'L': '555',
#     'M': '6', 'N': '66', 'O': '666',
#     'P': '7', 'Q': '77', 'R': '777', 'S': '7777',
#     'T': '8', 'U': '88', 'V': '888',
#     'W': '9', 'X': '99', 'Y': '999', 'Z': '9999',
#     ' ': '0'
# }
#
# # Вводим текстовое сообщение
# message = input().upper()  # Приводим к верхнему регистру для обработки
#
# # Проходим по буквам сообщения и выводим соответствующие нажатия клавиш
# for letter in message:
#     if letter in letter_to_keypress:
#         print(letter_to_keypress[letter], end='')
#     else:
#         print(' ', end='')  # Пробел для символов, не указанных в таблице
# print()  # Переход на новую строку



# ''' or '''
#
# d = {".": '1', ",": '11', "?": '111', "!": '1111', ":": '11111',
#      "A": '2', "B": '22', "C": '222',
#      "D": '3', "E": '33', "F": '333',
#      "G": '4', "H": '44', "I": '444',
#      "J": '5', "K": '55', "L": '555',
#      "M": '6', "N": '66', "O": '666',
#      "P": '7', "Q": '77', "R": '777', "S": '7777',
#      "T": '8', "U": '88', "V": '888',
#      "W": '9', "X": '99', "Y": '999', "Z": '9999',
#      " ": '0'
#      }
# s = tuple(input().upper().replace('"', ''))
#
# for i in s:
#     print(d[i], end='')


# ''' or '''
#
# d={".":'1', ",":'11', "?":'111', "!":'1111', ":":'11111',
#     "A":'2', "B":'22', "C":'222',
#     "D":'3', "E":'33', "F":'333',
#     "G":'4', "H":'44', "I":'444',
#     "J":'5', "K":'55', "L":'555',
#     "M":'6', "N":'66', "O":'666',
#     "P":'7', "Q":'77', "R":'777', "S": '7777',
#     "T":'8', "U":'88', "V":'888',
#     "W":'9', "X":'99', "Y":'999', "Z": '9999',
#     " ":'0'
# }
#
# for wd in input().upper():
#     print(d.get(wd, ""), end="")




# ''' Код Морзе '''
#
#
# letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
# morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---',
#          '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---',
#          '...--', '....-', '.....', '-....', '--...', '---..', '----.']
#
# morse_code = dict(zip(letters, morse))
# s = [i for i in input().upper() if i.isalnum()]
# for i in s:
#     print(morse_code.get(i, ''), end=' ')


# ''' or '''
#
# letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
#
# morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---',
#          '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---',
#          '...--', '....-', '.....', '-....', '--...', '---..', '----.']
#
# d_morse = dict(zip(letters, morse))
# n = input().upper()
# print(*[d_morse[i] for i in n if i in d_morse])



