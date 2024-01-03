






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
