''' функции без параметров'''

# ''' выводит звездный прямоугольник с размерами 14 × 10 '''

## объявление функции
# def draw_box():
#     for i in range(13):
#         if i > 0 and i < 13:
#             print('*        *')
#         if i == 0:
#             print('*' * 10)
#
#     else:
#         print('*' * 10)
# # основная программа
# draw_box()  # вызов функции
#
# ''' или '''
#
# # объявление функции
# def draw_box():
#     print("*" * 10)
#
#     for i in range(12):
#         print("*", "*", sep=" " * 8)
#
#     print("*" * 10)
#
#
# # основная программа
# draw_box()  # вызов функции


# ''' выводит звездный прямоугольный треугольник с катетами, равными 10 '''
#
# # объявление функции
# def draw_triangle():
#     for i in range(11):
#         print(i * '*')
#
# # основная программа
# draw_triangle()  # вызов функции


# ''' или '''
#
# # объявление функции
# def draw_triangle():
#     print(*['*' * i for i in range(1, 11)], sep='\n')
#
# # основная программа
# draw_triangle()  # вызов функции