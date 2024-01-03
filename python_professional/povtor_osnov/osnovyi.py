''' Функция hide_card() '''

def hide_card(card_number):
    """
    Функция hide_card принимает в качестве аргумента номер банковской карты card_number (строка)
    и заменяет первые 12 цифр на символ *, удаляя все пробелы.
    """
    card_number = card_number.replace(' ', '')  # удалить пробелы
    return '*' * 12 + card_number[12:]  # замена первых 12 цифр на *

# проверка работы функции
print(hide_card(input()))  # выводит: '************4567'



''' Функция same_parity() '''

def same_parity(numbers):
    # Если список пустой, возвращаем пустой список
    if not numbers:
        return []
    # Определение четности первого числа в списке
    parity = numbers[0] % 2
    # Создаем и возвращаем новый список, который включает числа с такой же четностью, что и первое число в исходном списке
    return [num for num in numbers if num % 2 == parity]

# Пример ввода данных
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Получение списка чисел с той же четностью, что и первое число, и вывод этого списка
result = same_parity(numbers)
print("Numbers with the same parity as the first number:", result)



''' Функция is_valid() '''

def is_valid(string):
    if 7 > len(string) > 3:
        if string.isdigit():
            if string.count(' ') == 0:
                return True
    return False


''' or '''

def is_valid(pin):
    return pin.isdigit() and len(pin) in (4, 5, 6)

''' or '''

def is_valid(pin: str) -> bool:
    return all((4 <= len(pin) <= 6, pin.isdigit()))




''' Функция print_given() '''

def print_given(*args, **kwargs):
    # вывод позиционных аргументов
    for arg in args:
        print(f"{arg} {type(arg)}")

    # вывод именованных аргументов в лексикографическом порядке
    for key in sorted(kwargs.keys()):
        print(f"{key} {kwargs[key]} {type(kwargs[key])}")

print_given(1, [1, 2, 3], 'three', two=2)


''' or '''

def print_given(*args, **kwargs):
    for arg in args:
        print(arg, type(arg))
    for name, value in sorted(kwargs.items()):
        print(name, value, type(value))



''' Функция convert() '''

def convert(string):
    # Подсчет количества букв в верхнем и нижнем регистрах
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())

    # Сравнение и преобразование строки
    if upper_count > lower_count:
        return string.upper()
    elif lower_count > upper_count:
        return string.lower()
    else:
        return string.lower()

# Пример использования
input_string = input()
result = convert(input_string)
print(result)


''' or '''


def convert(text):
    lower_count = len(list(filter(str.islower, text)))
    upper_count = len(list(filter(str.isupper, text)))
    if lower_count >= upper_count:
        return text.lower()
    return text.upper()


''' or '''

def convert(string):
    if sum(1 if c.isupper() else -1 for c in string if c.isalpha()) > 0:
        return string.upper()
    return string.lower()




''' Функция filter_anagrams() '''

from collections import Counter


def filter_anagrams(word, words):
    return [x for x in words if Counter(word) == Counter(x)]


word = 'abba'
words = ['aabb', 'abcd', 'bbaa', 'dada']

print(filter_anagrams(word, words))


''' or '''

def filter_anagrams(word, anagrams):
    return [anagram for anagram in anagrams if sorted(anagram) == sorted(word)]


''' or '''

def filter_anagrams(word, anagrams):
    return(list(filter(lambda x: sorted(x) == sorted(word), anagrams)))





''' Функция likes() '''

def likes(names):
    if len(names) == 0:
        return "Никто не оценил данную запись"
    elif len(names) == 1:
        return f"{names[0]} оценил(а) данную запись"
    elif len(names) == 2:
        return f"{names[0]} и {names[1]} оценили данную запись"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} и {names[2]} оценили данную запись"
    else:
        return f"{names[0]}, {names[1]} и {len(names) - 2} других оценили данную запись"

# Примеры использования
print(likes([]))
print(likes(['Тимур']))
print(likes(['Тимур', 'Артур']))
print(likes(['Тимур', 'Артур', 'Руслан']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима', 'Рома', 'Гвидо', 'Марк']))





''' Функция index_of_nearest() '''

def index_of_nearest(numbers, number):
    if not numbers:  # если список пуст, возвращаем None
        return -1
    # находим индекс минимального элемента по абсолютному значению разницы
    return min(range(len(numbers)), key=lambda index: abs(numbers[index] - number))

print(index_of_nearest([7, 13, 3, 5, 18], 0))


''' or '''

def index_of_nearest(nums, n):
    if nums:
        minimum = min(nums, key=lambda num: abs(num - n))
        return nums.index(minimum)
    return -1



''' Функция spell() '''

def spell(*args):
    return {i.lower()[0]: len(i) for i in sorted(args, key=len)}


words = ['Россия', 'Австрия', 'Австралия', 'РумыниЯ', 'Украина', 'КИТай', 'УЗБЕКИСТАН']
print(spell(*words))


''' or '''

def spell(*args):
    result = {}
    for word in args:
        if result.get(word[0].lower(), 0) < len(word):
            result[word[0].lower()] = len(word)
    return result




''' Функция choose_plural() 🌶️🌶️ '''

def choose_plural(amount, declensions):
    if amount % 10 == 1 and amount % 100 != 11:
        correct_word = declensions[0]
    elif 2 <= amount % 10 <= 4 and (amount % 100 < 10 or amount % 100 >= 20):
        correct_word = declensions[1]
    else:
        correct_word = declensions[2]

    return "{} {}".format(amount, correct_word)

print(choose_plural(21, ('пример', 'примера', 'примеров')))
print(choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей')))
print(choose_plural(8, ('яблоко', 'яблока', 'яблок')))
print(choose_plural(111223, ('копейка', 'копейки', 'копеек')))
print(choose_plural(763434, ('рубль', 'рубля', 'рублей')))
print(choose_plural(512312, ('цент', 'цента', 'центов')))
print(choose_plural(59, ('помидор', 'помидора', 'помидоров')))
print(choose_plural(23424157, ('огурец', 'огурца', 'огурцов')))
print(choose_plural(240, ('курица', 'курицы', 'куриц')))
print(choose_plural(49324, ('плюмбус', 'плюмбуса', 'плюмбусов')))
print(choose_plural(505, ('утка', 'утки', 'уток')))
print(choose_plural(666, ('шкаф', 'шкафа', 'шкафов')))
print(choose_plural(11, ('стул', 'стула', 'стульев')))
print(choose_plural(3458438435812, ('доллар', 'доллара', 'долларов')))




''' Функция get_biggest() 🌶️🌶️ '''


def get_biggest(numbers):
    if numbers:
        s = ''
        max_len_num = len(str(max(numbers)))
        numbers = sorted([str(i) for i in numbers], reverse=True, key=lambda x: x * max_len_num)
        return int(s.join(numbers))
    return -1



''' or '''

class new_str(str):
    def __lt__(self, other):
        return int(f'{self}{other}') < int(f'{other}{self}')


def get_biggest(numbers):
    if not numbers:
        return -1
    numbers = [new_str(n) for n in numbers]
    return int(''.join(sorted(numbers)[::-1]))




''' Тимур, Артур и новый курс '''


d1, d2, d3 = [int(input()) for _ in range(3)]
print(min(d1 + d3 + d2, d1 + d1 + d2 + d2, d2 + d3 + d3 + d2, d1 + d3 + d3 + d1))


''' or '''

lst = sorted([int(input()) for i in range(3)])
if sum(lst[:2]) * 2 < sum(lst):
    print(sum(lst[:2]) * 2)
else:
    print(sum(lst))


''' or '''


lst = sorted(int(input()) for _ in range(3))

print(min(sum(lst), sum(lst[:2]) * 2))



''' Схожие буквы '''


langs = ['ru', 'mix', 'mix', 'en']
eng = 'AaBCcEeHKMOoPpTXxy'
index = sum([input() in eng for i in range(3)])
print(langs[index])


