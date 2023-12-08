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

