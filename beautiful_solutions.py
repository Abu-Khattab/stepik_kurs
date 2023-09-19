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
