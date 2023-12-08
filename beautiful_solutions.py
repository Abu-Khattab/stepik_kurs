# ''' Шифр Цезаря 🌶️ '''
#
# n = int(input())
# s = input()
#
# for el in s:
#     cur_n = ord("a") + (ord(el) - ord("a") + 26 - n) % 26
#     print(chr(cur_n), end="")


# s = [int(i) for i in s] - простой способ преобразовать список str в список int


# l = [int(i) for i in input().split()] # способ преобразовать список str в список int




# def is_palindrome(number):
#     # Функция для проверки, является ли число палиндромом
#     return str(number) == str(number)[::-1]

# def is_prime(number):
#     # Функция для проверки, является ли число простым
#     if number <= 1:
#         return False
#     for i in range(2, int(number**0.5) + 1):
#         if number % i == 0:
#             return False
#     return True

# def is_valid_password(password):
#     # Разбиваем пароль на a, b и c
#     parts = password.split(":")
#     if len(parts) != 3:
#         return False
#
#     a, b, c = map(int, parts)
#
#     # Проверяем условия
#     if is_palindrome(a) and is_prime(b) and c % 2 == 0:
#         return True
#     else:
#         return False


# # Пример использования функции
# password = input()
# result = is_valid_password(password)
# if result:
#     print("Пароль действителен")
# else:
#     print("Пароль не действителен")



# ''' функция для проверки чёт или нечёт число '''
# def even_or_odd(number):
#   return ["Even", "Odd"][number % 2]

# ''' определяет, оканчивается ли год с данным номером на два нуля '''
#
# print('YES' if int(input()) % 100 == 0 else 'NO')



# {int(_) for _ in input().split()}  # оказывается, можно еще сразу так))



# ''' ля каждого символа строки text будет подсчитано количество его вхождений. '''
#
# text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
#
# result = {}
#
# for i in text:
#     result[i] = result.get(i, 0) + 1
#
# print(result)


# {value:key for key, value in result.items()} # меняет местами ключ и значение в словаре. Может кому нибудь поможет.


# lst = [word.strip('.,!?:;-') for word in input().lower().split()]  # Получить список очищенных  слов



# ''' Возврат уникальных чисел из массива '''
#
#
# def removeDuplicates(nums):
#     if not nums:
#         return 0
#
#     k = 1  # Индекс, указывающий на текущую уникальную позицию в массиве
#
#     for i in range(1, len(nums)):
#         if nums[i] != nums[i - 1]:
#             nums[k] = nums[i]
#             k += 1
#
#     return k
#
#
# # Пример использования
# nums = [1, 1, 2, 2, 2, 3, 3, 4, 5, 5]
# k = removeDuplicates(nums)
# print(nums[:k])  # Вывод уникальных элементов
# print(k)  # Вывод количества уникальных элементов




# ''' Однако есть проблема: когда мы находимся на последнем студенте в списке, (i + 1) выходит за
# пределы диапазона списка (поскольку индекс последнего студента равен len(list_of_students) - 1).
#
# Для решения этой проблемы мы используем оператор % (взятие по модулю).
# (i + 1) % len(list_of_students) гарантирует, что мы остаемся в пределах диапазона списка.
# Когда (i + 1) достигает значения len(list_of_students), возвращается к 0,
# таким образом, обеспечивается циклическая обработка списка. '''
#
#
# stud_quantity = int(input())
# list_of_students = []
# for i in range(stud_quantity):
#     students = input()
#     list_of_students.append(students)
#
# for i in range(len(list_of_students)):
#     print(f'{list_of_students[i]} - {list_of_students[(i + 1) % len(list_of_students)]}')


# такая конструкция вытянет по одному случайному символу из всех 3 указанных списков
# result = [choice(i) for i in (chars1, chars2, chars3)]


# ''' isinstance() - это встроенная функция Python, которая позволяет проверить тип объекта.
# Если arg является числом (int или float), условие вернет True, и arg будет включен в numeric_args.'''
#
# numeric_args = [arg for arg in args if isinstance(arg, (int, float))]
# numeric_args = [i for i in args if type(i) in (int, float)]



# def fun(x):
#     x = [int(i) for i in str(x)]
#     return sum(x)
#
#
# numbers = input().split()  # Считываем список чисел
# result = [fun(int(num)) for num in numbers]  # Применяем fun к каждому числу
# print(result)  # Выводим результат



def MAP(func, items):
    return [func(item) for item in items]



def FILTER(func, items):
    return [item for item in items if func(item)]


''' max - min '''

list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
maximum = max(map(max, list1))

print(maximum)


''' создать матрицу '''

n = int(input())
matrix = [input().split() for _ in range(n)]


