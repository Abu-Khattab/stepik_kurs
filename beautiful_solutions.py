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