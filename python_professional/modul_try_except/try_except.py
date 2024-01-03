

# blog_posts = [{'Photos': 3, 'Likes': 21, 'Comments': 2},
#               {'Likes': 13, 'Comments': 2, 'Shares': 1},
#               {'Photos': 5, 'Likes': 33, 'Comments': 8, 'Shares': 3},
#               {'Comments': 4, 'Shares': 2},
#               {'Photos': 8, 'Comments': 1, 'Shares': 1},
#               {'Photos': 3, 'Likes': 19, 'Comments': 3}]
#
# total_likes = 0
#
#
#
# for post in blog_posts:
#     try:
#         total_likes += post['Likes']
#     except:
#         total_likes += post.get('Likes', -1)
#
# print(total_likes)




# food = ['chocolate', 'chicken', 'corn', 'sandwich', 'soup', 'potatoes', 'beef', 'lox', 'lemonade']
# fifth = []
#
# for x in food:
#     try:
#         if len(x) > 4:
#             fifth.append(x[4])
#         else:
#             fifth.append('_')
#     except ValueError:
#         pass
# print(fifth)





# numbers = [6, 0, 36, 8, 2, 36, 0, 12, 60, 0, 45, 0, 3, 23]
#
# remainders = []
#
# for number in numbers:
#     try:
#         remainders.append(36 % number)
#     except ZeroDivisionError:
#         pass
#
# print(remainders)







# ''' only numbers '''




# import sys
#
#
#
# sum_of_numbers = 0
# count_of_non_numbers = 0
#
# for line in sys.stdin:
#     line = line.strip()
#     try:
#         # Попытка преобразовать введенное значение в число
#         number = float(line)
#
#         # Если успешно, добавляем к сумме
#         sum_of_numbers += number
#     except ValueError:
#         # Если введенное значение не является числом, увеличиваем счетчик нечисловых значений
#         count_of_non_numbers += 1
#
# print({sum_of_numbers if sum_of_numbers % 1 != 0 else int(sum_of_numbers)})
#
# print(count_of_non_numbers)




# ''' or '''



# import sys
#
# def main():
#     sum_of_numbers = 0
#     count_of_non_numbers = 0
#
#     for line in sys.stdin:
#         line = line.strip()
#
#         try:
#             number = float(line)
#             sum_of_numbers += number
#         except ValueError:
#             count_of_non_numbers += 1
#
#     print(f"Сумма введенных чисел: {sum_of_numbers}")
#     print(f"Количество нечисловых значений: {count_of_non_numbers}")
#
# if __name__ == "__main__":
#     main()






# ''' Январь, февраль, ... '''



# # Импортируем модуль календаря
# import calendar
#
# try:
#     # Запрашиваем у пользователя номер месяца и преобразуем его в целое число
#     month_num = int(input("Введите номер месяца: "))
#
#     # Проверяем, что номер месяца находится в допустимом диапазоне от 1 до 12
#     if 1 <= month_num <= 12:
#         # Если номер месяца в допустимом диапазоне, выводим название месяца
#         print(calendar.month_name[month_num])
#     else:
#         # Если номер месяца не в допустимом диапазоне, выводим сообщение об ошибке
#         print("Введено число из недопустимого диапазона")
# except ValueError:
#     # Если введенное значение не может быть преобразовано в целое число, выводим сообщение об ошибке
#     print("Введено некорректное значение")




# '''  Функция add_to_list_in_dict() '''
#
#
# def add_to_list_in_dict(data, key, element):
#     try:
#         data[key].append(element)
#     except:
#         data[key] = [element]
#
#
# data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
# add_to_list_in_dict(data, 'b', 7)
#
# print(data)
#





''' readme.txt '''


# Определение функции для чтения файла
def read_file(filename):
    # Блок try для обработки исключений
    try:
        # Открываем файл в режиме чтения с указанием кодировки UTF-8
        with open(filename, 'r', encoding='utf-8') as file:
            # Читаем и выводим содержимое файла
            print(file.read())
    # Если файл не найден, обрабатываем исключение FileNotFoundError
    except FileNotFoundError:
        # Выводим сообщение о том, что файл не найден
        print('Файл не найден')

# Вызов функции для чтения файла
read_file(input())





