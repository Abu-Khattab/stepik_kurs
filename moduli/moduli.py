# ''' принимает два обязательных аргумента a и b
# и возвращает случайное целое число из отрезка [a;b].'''
#
# import random
#
# num1 = random.randint(0, 17)
# num2 = random.randint(-5, 5)
#
# print(num1)
# print(num2)


# ''' выводит 10 случайных целых чисел из диапазона [1;100]: '''
#
# import random
#
# for _ in range(10):
#     print(random.randint(1, 100))


# import random
#
# print('Бросаем кубики... ')
# print('Значения граней:')
# print(random.randint(1, 6))
# print(random.randint(1, 6))



# import random
#
# again = 'д'
# while again.lower() == 'д':
#     print('Бросаем кубики... ')
#     print('Значения граней:')
#     print(random.randint(1, 6))
#     print(random.randint(1, 6))
#     again = input('Бросить кубики еще раз? (д = да, н = нет): ')


# import random
#
# for _ in range(10):
#     num = random.randint(0, 1)
#     if num == 0:
#         print('Орел')
#     else:
#         print('Решка')


# ''' принимает список в качестве обязательного аргумента и перемешивает его случайным образом. '''
#
# import random
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# random.shuffle(numbers)
# print(numbers)


# ''' принимает список (строку) в качестве обязательного аргумента
# и возвращает один случайный элемент из переданного списка (строки).'''
#
#
# import random
#
# print(random.choice('BEEGEEK'))
# print(random.choice([1, 2, 3, 4]))
# print(random.choice(['a', 'b', 'c', 'd']))


# ''' принимает два обязательных аргумента: список (строку) и количество случайных элементов,
# а возвращает список случайных элементов в указанном количестве. '''
#
# import random
#
# numbers = [2, 5, 8, 9, 12]
#
# print(random.sample(numbers, 1))
# print(random.sample(numbers, 2))
# print(random.sample(numbers, 3))
# print(random.sample(numbers, 5))