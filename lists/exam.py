
# ''' Каждый n-ый элемент '''
#
# def split_list(input_list, n):
#     s = [[] * n for _ in range(n)]
#     for i in range(n):
#         for j in range(i, len(input_list), n):
#             s[i].append(input_list[j])
#     print(s)
#
# input_string = input().split()
# n = int(input())
#
#
# split_list(input_string, n)
#
#
# ''' or '''
#
# symbols = input().split()
# n = int(input())
# result = [[] for _ in range(n)]
#
# for i in range(len(symbols)):
#     result[i % n].append(symbols[i])
#
# print(result)
#
#
# ''' or '''
#
#
# s = input().split()
# n = int(input())
# res = []
# for i in range(n):
#     res.append(s[i::n])
# print(res)




# ''' Максимальный в области 2 '''
#
#
# n = int(input())
# matrix = []
# for k in range(n):
#     tmp = [int(x) for x in input().split()]
#     matrix.append(tmp)
#
# Max = matrix[0][0]
#
# for i in range(n):
#     for q in range(n):
#         if i >= n - 1 - q and matrix[i][q] > Max:
#             Max = matrix[i][q]
# print(Max)
#
#
# ''' or '''
#
#
# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# largest = matrix[0][n - 1]
#
# for i in range(n):
#     for j in range(n):
#         if i + j + 1 >= n and matrix[i][j] > largest:
#             largest = matrix[i][j]
#
# print(largest)




# ''' Транспонирование матрицы '''
#
#
# n = int(input())
# matrix = []
# for i in range(n):
#     tmp = [int(x) for x in input().split()]
#     matrix.append(tmp)
# print()
#
# for i in range(n):
#     for j in range(n):
#         print(matrix[j][i], end=' ')
#     print()
#
#
#
# ''' or '''
#
#
# n = int(input())
# matrix = [input().split() for _ in range(n)]
#
# for i in range(n):
#     for j in range(i, n):
#         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#
# for row in matrix:
#     print(*row)





# ''' Снежинка '''
#
# n = int(input())
# matrix = []
# for _ in range(n):
#     tmp = ['.' for x in range(n)]
#     matrix.append(tmp)
#
# for i in range(n):
#     for q in range(n):
#         if i == q or i == n - 1 - q:
#             matrix[i][q] = '*'
#         elif n // 2 == i or n // 2 == q:
#             matrix[i][q] = '*'
#
# for i in range(n):
#     print(*matrix[i])
#
#
#
# ''' or '''
#
# n = int(input())
# matrix = [["." for _ in range(n)] for _ in range(n)]
#
# for i in range(n):
#     # для главной диагонали
#     matrix[i][i] = "*"
#     # для побочной диагонали
#     matrix[i][n - 1 - i] = "*"
#     # для средней строки
#     matrix[n // 2][i] = "*"
#     # для среднего столбца
#     matrix[i][n // 2] = "*"
#
# for row in matrix:
#     print(*row)
#
#
# ''' or '''
#
# n = int(input())
# matrix = [['.'] * n for _ in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         if i == n // 2 or j == n // 2:
#             matrix[i][j] = '*'
#         elif i == j or i + j + 1 == n:
#             matrix[i][j] = '*'
#
# for row in matrix:
#     print(*row)




# ''' Симметричная матрица '''
#
# n = int(input())
# matrix = []
# flag = True
#
# for _ in range(n):
#     tmp = [int(x) for x in input().split()]
#     matrix.append(tmp)
# matrix.reverse()
#
#
# for i in range(n):
#     for q in range(n):
#         if matrix[i][q] != matrix[q][i]:
#             flag = False
#             break
#
# if flag:
#     print('YES')
# else:
#     print('NO')
#
#
# ''' or '''
#
#
# def is_symmetric(matrix):
#     for i in range(n):
#         for j in range(n - i - 1):
#             if matrix[i][j] != matrix[n - 1 - j][n - 1 - i]:
#                 return "NO"
#
#     return "YES"
#
#
# n = int(input())
# matrix = [input().split() for _ in range(n)]
#
# print(is_symmetric(matrix))




# '''  Латинский квадрат 🌶️ '''
#
# n = int(input())
# matrix = []
# flag = True
#
# for _ in range(n):
#     tmp = [int(x) for x in input().split()]
#     matrix.append(tmp)
# latin_list = [i for i in range(1, n + 1)]
#
# for i in range(n):
#     x = sorted(matrix[i])
#     y = sorted([matrix[q][i] for q in range(n)])
#     if x != latin_list or y != latin_list:
#         flag = False
#         break
#
#
# if flag:
#     print('YES')
# else:
#     print('NO')
#
#
#
# ''' or '''
#
# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# numbers = list(range(1, n + 1))
# result = 'YES'
#
# for i in range(n):
#     row_nums = sorted(matrix[i])
#     col_nums = sorted([matrix[j][i] for j in range(n)])
#     if row_nums != numbers or col_nums != numbers:
#         result = 'NO'
#         break
#
# print(result)
#
#
# ''' or '''
#
#
# n = int(input())
# matrix = [[int(x) for x in input().split()] for _ in range(n)]
# for i in range(n):
#     if sorted(matrix[i]) != list(range(1, n + 1)) or sorted([matrix[j][i] for j in range(n)]) != list(range(1, n + 1)):
#         print('NO')
#         break
# else:
#     print('YES')




# ''' Ходы ферзя '''
#
# x, y = input()
# n = 8
# matrix = [['.'] * n for _ in range(n)]
# y = n - int(y)
# x = ord(x) - 97
#
# for i in range(n):
#     for q in range(n):
#         if i == y or q == x:
#             matrix[i][q] = '*'
#         elif (i + q == y + x) or (i - q == y - x):
#             matrix[i][q] = '*'
#
#
# matrix[y][x] = 'Q'
#
# for x in range(n):
#     print(*matrix[x])
#
#
#
# ''' or '''
#
# x, y = input()
# n = 8
# board = [['.'] * n for _ in range(n)]
# x = ord(x) - 97
# y = n - int(y)
#
# for i in range(n):
#     for j in range(n):
#         if i == y or j == x:
#             board[i][j] = '*'
#         elif abs(i - y) == abs(j - x):
#             board[i][j] = '*'
#
# board[y][x] = 'Q'
#
# for row in board:
#     print(*row)




# ''' Диагонали, параллельные главной '''
#
#
# n = int(input())
# matrix = [[0 for _ in range(n)] for _ in range(n)]  # Create a 2D list
#
# for i in range(n):
#     for q in range(n):
#         if q > i:
#             matrix[i][q] = q - i
#         if i > q:
#             matrix[i][q] = i - q
#
# for i in range(n):
#     print(*matrix[i])
#
#
#
# ''' or '''
#
# n = int(input())
# matrix = [[abs(i - j) for j in range(n)] for i in range(n)]
#
# for row in matrix:
#     print(*row)
#