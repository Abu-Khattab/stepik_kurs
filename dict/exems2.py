'''exems'''


''' часть 1 '''

my_dict = {'C1': [10, 20, 30, 7, 6, 23, 90], 'C2': [20, 30, 40, 1, 2, 3, 90, 12], 'C3': [12, 34, 20, 21],
           'C4': [22, 54, 209, 21, 7], 'C5': [2, 4, 29, 21, 19], 'C6': [4, 6, 7, 10, 55], 'C7': [4, 8, 12, 23, 42],
           'C8': [3, 14, 15, 26, 48], 'C9': [2, 7, 18, 28, 18, 28]}


result = {key: [i for i in my_dict[key] if i <= 20] for key in my_dict}
print(result)


''' часть 1/2 '''

emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
          'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
          'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
          'yandex.ru': ['surface', 'google'],
          'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
          'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}


result = sorted(i + '@' + key for key, values in emails.items() for i in values)
print(*result, sep='\n')


''' or '''

emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
          'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
          'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
          'yandex.ru': ['surface', 'google'],
          'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
          'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}

print(*sorted(f"{name}@{domain}" for domain in emails for name in emails[domain]), sep='\n')



''' Минутка генетики '''

d = {'ACGT'[i]: 'UGCA'[i] for i in range(4)}
for i in input():
    print(d[i], end='')


''' or '''

ils = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}


result = [ils[i] for i in input()]
print(*result, end='')



''' Порядковый номер '''

words = input().split()
result = {}

for word in words:
    result[word] = result.get(word, 0) + 1
    print(result[word], end=' ')


''' or '''

words = input().split()
print(*[words[:i+1].count(words[i]) for i in range(len(words))])





''' Scrabble game '''



def scrabble_score(word):
    d = {
        1: "AEILNORSTU",
        2: "DG",
        3: "BCMP",
        4: "FHVWY",
        5: "K",
        8: "JX",
        10: "QZ"
    }

    # Преобразование слова в верхний регистр для удобства
    word = word.upper()

    # Инициализация счетчика стоимости
    total_score = 0

    # Итерация по каждой букве в слове
    for letter in word:
        # Ищем, к какой категории буква принадлежит, и прибавляем соответствующие баллы
        for score, letters in d.items():
            if letter in letters:
                total_score += score

    return total_score

# Чтение входного слова
input_word = input()

# Вызов функции для подсчета стоимости и вывод результата
result = scrabble_score(input_word)
print(result)



''' or '''


my_dict = {
        1: "AEILNORSTU",
        2: "DG",
        3: "BCMP",
        4: "FHVWY",
        5: "K",
        8: "JX",
        10: "QZ"
    }

s = input().upper()
result = [key for letter in s for key, value in my_dict.items() if letter in value]
print(sum(result))



''' or '''



d = {
    1: "AEILNORSTU",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ"
}

print(sum([k for i in input() for k, v in d.items() if i in v]))





''' Строка запроса '''


def build_query_string(params):
    # Сортируем ключи словаря в лексикографическом порядке
    sorted_keys = sorted(params.keys())

    # Создаем список строк для представления каждого параметра
    param_strings = []

    # Итерируемся по отсортированным ключам
    for key in sorted_keys:
        # Получаем значение по ключу
        value = params[key]

        # Преобразуем ключ и значение в строку и добавляем их в список
        param_strings.append(f"{key}={value}")

    # Используем символ амперсанда для объединения строк из списка в единую строку запроса
    query_string = "&".join(param_strings)

    return query_string

# Примеры использования функции
query1 = build_query_string({'name': 'timur', 'age': 28})
query2 = build_query_string({'sport': 'hockey', 'game': 2, 'time': 17})

# Выводим результаты
print(query1)  # Должно вывести: age=28&name=timur
print(query2)  # Должно вывести: game=2&sport=hockey&time=17



''' or '''


def build_query_string(params):
    res = [f'{k}={v}' for k, v in params.items()]
    return '&'.join(sorted(res))




''' Слияние словарей 🌶️ '''


def merge(list_of_dicts):
    result = {}  # Создаем пустой словарь для хранения результата
    for d in list_of_dicts:  # Итерируемся по каждому словарю в списке
        for key, value in d.items():  # Итерируемся по каждой паре ключ-значение в словаре
            result.setdefault(key, set()).add(value)
            # setdefault(key, set()) создает множество для ключа, если его нет
            # add(value) добавляет значение в это множество
    return result  # Возвращаем полученный словарь

# Пример использования:
result = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])

print(result)
# Выведет: {'a': {1, 5}, 'b': {2, 10, 17}, 'c': {50, 100}, 'd': {777}}


''' or '''

def merge(values):
    res = {}
    for d in values:
        for k, v in d.items():
            res.setdefault(k, set()).add(v)
    return res




''' Опасный вирус 😈 '''


result = {}
dict_operations = {'W' : 'write', 'R' : 'read', 'X' : 'execute'}

for _ in range(int(input())):
    x = input().split()
    result[x[0]] = [dict_operations[i] for i in x[1:]]

for _ in range(int(input())):
    x = input().split()
    if x[0] in result[x[1]]:
        print("OK")
    else:
        print("Access denied")



''' or '''

transform = {'execute': 'X', 'write': 'W', 'read': 'R'}
mydict = {}

for _ in range(int(input())):
    name, *operations = input().split()
    mydict[name] = operations

for _ in range(int(input())):
    operation, name = input().split()
    if transform[operation] in mydict[name]:
        print('OK')
    else:
        print('Access denied')




''' Покупки в интернет-магазине 🌶️ '''


from collections import defaultdict

def count_items(data):
    # Используем defaultdict для хранения данных о покупках
    purchases = defaultdict(lambda: defaultdict(int))

    # Заполняем purchases данными из входных данных
    for line in data:
        # Разбиваем строку на отдельные части: покупатель, товар и количество
        buyer, item, quantity = line.split()
        # Увеличиваем счетчик товара для данного покупателя
        purchases[buyer][item] += int(quantity)

    # Сортируем и выводим результат
    buyers = sorted(purchases.keys())
    for buyer in buyers:
        print(f"{buyer}:")
        # Сортируем товары для данного покупателя
        items = sorted(purchases[buyer].keys())
        for item in items:
            # Выводим информацию о количестве каждого товара
            print(f"  {item}: {purchases[buyer][item]}")

# Чтение входных данных
n = int(input())
input_data = [input() for _ in range(n)]

# Вызов функции для обработки данных и вывода результата
count_items(input_data)




''' or '''


database = {}
for _ in range(int(input())):
    name, good, amount = input().split()
    database[name][good] = database.setdefault(name, {}).get(good, 0) + int(amount)

for name, goods in sorted(database.items()):
    print(name + ':')
    for good, amount in sorted(goods.items()):
        print(good, amount)




''' exems end '''