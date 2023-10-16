# fruits = ["apples", "bananas", "strawberry"]
# new_fruit = []
# for fruit in fruits:
#     fruit = fruit.upper()
#     new_fruit.append(fruit)
#
#
# print(new_fruit)
#
#
# ''' or '''
#
# fruit_components = [fruit.upper() for fruit in fruits]
#
# print(fruit_components)


# ''' Ключом будет позиция числа в списке numbers, а значением – его квадрат. '''
#
# # numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]
# #
# # result = {i: numbers[i] ** 2 for i in range(len(numbers))}
# # print(result)



# ''' словарь result, состоящий из всех элементов словаря colors, кроме тех,
#     у которых значением является None.'''
#
# colors = {'c1': 'Red', 'c2': 'Grey', 'c3': None,
#           'c4': 'Green', 'c5': 'Yellow', 'c6': 'Pink', 'c7': 'Orange', 'c8': None,
#           'c9': 'White', 'c10': 'Black', 'c11': 'Violet', 'c12': 'Gold', 'c13': None,
#           'c14': 'Amber', 'c15': 'Azure', 'c16': 'Beige', 'c17': 'Bronze', 'c18': None,
#           'c19': 'Lilac', 'c20': 'Pearl', 'c21': None,
#           'c22': 'Sand', 'c23': None}
#
# result = {i: colors[i] for i in colors if colors[i] is not None}

# or
# result = {x: colors[x] for x in colors if colors[x]}
#
# print(result)



# ''' словарь result, состоящий из всех элементов словаря favorite_numbers ,
#     значения которых являются двузначными числами.'''
#
# favorite_numbers = {'timur': 17, 'ruslan': 7, 'larisa': 19, 'roman': 123, 'rebecca': 293, 'ronald': 76, 'dorothy': 62,
#                     'harold': 36, 'matt': 314, 'kim': 451, 'rosaly': 18, 'rustam': 89, 'soltan': 111, 'amir': 654,
#                     'dima': 390, 'amiran': 777, 'geor': 999, 'sveta': 75, 'rita': 909, 'kirill': 404, 'olga': 271,
#                     'anna': 55, 'madlen': 876}
#
# result = {key: value for key, value in favorite_numbers.items() if 9 < value <= 99}
#
# # or # result = {k : v for k, v in f.items() if len(str(v)) == 2}
# print(result)



''' словарь months , в которых ключ и значение поменялись местами. '''

months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

result = {value: key for key, value in months.items()}
print(result)