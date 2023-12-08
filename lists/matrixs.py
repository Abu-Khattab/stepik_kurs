

''' Таблица умножения '''

n, m = int(input()), int(input())
matrix = []

for k in range(n):
    tmp = [x for x in range(m)]
    matrix.append(tmp)

for i in range(n):
    for q in range(m):
        matrix[i][q] = i * q

for i in range(n):
    for q in range(m):
        print(str(matrix[i][q]).ljust(3), end=' ')
    print()




''' Максимум в таблице '''

n, m = int(input()), int(input())
matrix = []

for k in range(n):
    tmp = [int(x) for x in input().split()]
    matrix.append(tmp)


x = 0
y = 0
matrix_max = matrix[0][0]

for i in range(n):
    for q in range(m):
        if matrix[i][q] > matrix_max:
            matrix_max = matrix[i][q]
            x = i
            y = q

print(x, y)



''' Обмен столбцов '''


n, m = int(input()), int(input())
matrix = []

for k in range(n):
    tmp = [int(x) for x in input().split()]
    matrix.append(tmp)


i, j = [int(i) for i in input().split()]


for x in range(n):
    matrix[x][i], matrix[x][j] = matrix[x][j], matrix[x][i]

for q in range(n):
    print(*matrix[q])



''' Симметричная матрица '''


n = int(input())
matrix = []

for k in range(n):
    tmp = [int(x) for x in input().split()]
    matrix.append(tmp)


def is_symmetric(matrix):
    rows = len(matrix)
    cols = len(matrix[0])


    # Проверяем симметричность
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != matrix[j][i]:
                return False

    return True


result = is_symmetric(matrix)

if result:
    print("YES")
else:
    print("NO")



''' Обмен диагоналей '''


n = int(input())
matrix = []

for k in range(n):
    tmp = [int(x) for x in input().split()]
    matrix.append(tmp)


for i in range(n):
    matrix[i][i], matrix[n - 1 - i][i] = matrix[n - 1 - i][i], matrix[i][i]


for q in range(n):
    print(*matrix[q])



''' Зеркальное отображение '''


n = int(input())
matrix = []

for k in range(n):
    tmp = [int(x) for x in input().split()]
    matrix.append(tmp)

# Обратный порядок строк
reversed_matrix = matrix[::-1]

for row in reversed_matrix:
    print(*row)



''' Поворот матрицы '''


n = int(input())
matrix = [input().split() for _ in range(n)]

for i in range(n):
    for q in range(n - 1, -1, -1):
        print(matrix[q][i], end=' ')

    print()



''' Ходы коня '''


x, y = input()
n = 8
matrix = [['.'] * n for _ in range(n)]
y = n - int(y)
x = ord(x) - 97
matrix[y][x] = 'N'

for i in range(n):
    for q in range(n):
        if abs(i - y) * abs(q - x) == 2:
            matrix[i][q] = '*'


for x in range(n):
    print(*matrix[x])



''' Магический квадрат 🌶️ '''


n = int(input())
matrix = []
for _ in range(n):
    tmp = [int(x) for x in input().split()]
    matrix.append(tmp)
digits = [i for i in range(1, n ** 2 + 1)]

d1, d2 = 0, 0

for i in range(n):
    stolb_sum, stroka_sum = 0, 0
    for j in range(n):
        stolb_sum += matrix[j][i]
        stroka_sum += matrix[i][j]
        if matrix[i][j] in digits:
            digits.remove(matrix[i][j])
    d1 += matrix[i][i]
    d2 += matrix[i][n - i - 1]
    if stolb_sum != stroka_sum:
        break

if stolb_sum == stroka_sum == d1 == d2 and digits == []:
    print("YES")
else:
    print("NO")



''' or '''


def is_magic_square(n, matrix):
    # создаем список для всех чисел правильной матрицы
    correct_nums = list(range(1, n ** 2 + 1))

    # создаем список для всех чисел нашей матрицы
    our_nums = []
    for row in matrix:
        our_nums.extend(row)

    # если эти списки не равны, значит наша матрица уже не состоит из всех чисел от 1 до n ** 2
    # значит, мы сразу можем вернуть "NO" и не продолжать дальнейшие проверки
    if sorted(our_nums) != correct_nums:
        return "NO"

    # в самой матрице мы уже храним все ряды (строки)
    rows = matrix.copy()

    # создаем список для всех столбцов
    columns = []
    for j in range(n):
        cur_column = []
        for i in range(n):
            cur_column.append(matrix[i][j])

        columns.append(cur_column)

    # создаем список для диагоналей (с двумя пустыми подсписками)
    diagonals = [[], []]
    for i in range(n):
        diagonals[0].append(matrix[i][i])
        diagonals[1].append(matrix[i][n - 1 - i])

    # соединям все строки, столбцы и диагонали в один список
    all_lines = rows + columns + diagonals

    # инициализируем переменные для максимальной и минимальной суммы среди всех "линий"
    # за начальные значения возьмём сумму первой "линии"
    max_sum = sum(all_lines[0])
    min_sum = sum(all_lines[0])
    for line in all_lines:
        max_sum = max(max_sum, sum(line))
        min_sum = min(min_sum, sum(line))

    # теперь просто сравниваем максимальную и минимальную суммы
    # они должны быть равны, т.к. все суммы должны быть равны
    if max_sum != min_sum:
        return "NO"

    return "YES"


n = int(input())
matrix = [[int(el) for el in input().split()] for _ in range(n)]

print(is_magic_square(n, matrix))




''' Шахматная доска '''


x = input().split()
n, m = (int(x[0]), int(x[1]))
matrix = []

for _ in range(n):
    tmp = [e for e in range(m)]
    matrix.append(tmp)

for i in range(n):
    for q in range(m):
        if (i + q) % 2 == 0:
            matrix[i][q] = '.'
        else:
            matrix[i][q] = '*'


for i in range(n):
    print(*matrix[i])



''' Побочная диагональ '''


n = int(input())
matrix = []

for _ in range(n):
    tmp = [e for e in range(n)]
    matrix.append(tmp)

for i in range(n):
    for q in range(n):
        if i == n - 1 - q:
            matrix[i][q] = 1
        elif i < n - 1 - q:
            matrix[i][q] = 0
        else:
            matrix[i][q] = 2

for i in range(n):
    print(*matrix[i])



''' Заполнение 1 '''


x = input().split()
n, m = (int(x[0]), int(x[1]))
matrix = []

for i in range(n):
    tmp = [i * m + q + 1 for q in range(m)]
    matrix.append(tmp)

for i in range(n):
    for q in range(m):
        print(str(matrix[i][q]).ljust(3), end=' ')
    print()



''' Заполнение 2 '''


x = input().split()
n, m = (int(x[0]), int(x[1]))
matrix = []

count = 1
for i in range(n):
    tmp = [count + q * n for q in range(m)]
    matrix.append(tmp)
    count += 1

for i in range(n):
    for q in range(m):
        print(str(matrix[i][q]).ljust(3), end=' ')
    print()


''' Заполнение 3 '''


n = int(input())
matrix = []

for i in range(n):
    row = [1 if j == i or j == n - i - 1 else 0 for j in range(n)]
    matrix.append(row)

for row in matrix:
    for element in row:
        print(element, end=' ')
    print()



'''  Заполнение 4 '''


''' Заполнение 5 🌶️ '''


x = input().split()
n, m = (int(x[0]), int(x[1]))
tmp = [e for e in range(1, m + 1)]
matrix = []

for i in range(n):
    matrix.append(tmp)
    tmp = tmp[1:] + [tmp[0]]


for i in range(n):
    for q in range(m):
        print(str(matrix[i][q]).ljust(3), end=" ")
    print()


''' Заполнение змейкой '''


x = input().split()
n, m = (int(x[0]), int(x[1]))
matrix = []

for _ in range(n):
    tmp = [e for e in range(m)]
    matrix.append(tmp)

count = 1
for i in range(n):
    for q in range(m):
        matrix[i][q] = count
        count += 1


for i in range(n):
    if i % 2 != 0:
        matrix[i].reverse()


for i in range(n):
    for q in range(m):
        print(str(matrix[i][q]).ljust(3), end=' ')
    print()




''' Заполнение диагоналями 🌶️ '''


n, m = map(int, input().split())
matrix = []

for _ in range(n):
    tmp = [e for e in range(m)]
    matrix.append(tmp)

count = 1
for k in range(n * m):
    for i in range(n):
        for j in range(m):
            if i + j == k:
                matrix[i][j] = count
                count += 1

for i in range(n):
    for q in range(m):
        print(str(matrix[i][q]).ljust(3), end=' ')
    print()



''' Заполнение спиралью 😈😈 '''

n, m = map(int, input().split())
matrix = [[0] * m for _ in range(n)]

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
current_direction = 0
current_position = (0, 0)

for i in range(1, n * m + 1):
    matrix[current_position[0]][current_position[1]] = i
    next_row, next_col = current_position[0] + directions[current_direction][0], current_position[1] + directions[current_direction][1]

    if 0 <= next_row < n and 0 <= next_col < m and matrix[next_row][next_col] == 0:
        current_position = (next_row, next_col)
    else:
        current_direction = (current_direction + 1) % 4
        current_position = (current_position[0] + directions[current_direction][0], current_position[1] + directions[current_direction][1])

for row in matrix:
    print(*row)



''' or '''

n, m = [int(i) for i in input().split()]

matrix = [[0] * m for _ in range(n)]
counter = 1
rows_passed, columns_passed = 0, 0
current_row, current_column = 0, 0

for k in range(n * m):
    if counter == n * m + 1:
        break
    direction = k % 4
    if direction == 0:
        for j in range(columns_passed, m - columns_passed):
            matrix[current_row][j] = counter
            counter += 1
        current_column = j
        rows_passed += 1
    elif direction == 1:
        for i in range(rows_passed, n - rows_passed + 1):
            matrix[i][current_column] = counter
            counter += 1
        current_row = i
        columns_passed += 1
    elif direction == 2:
        for j in range(current_column - 1, columns_passed - 2, -1):
            matrix[current_row][j] = counter
            counter += 1
        current_column = j
    elif direction == 3:
        for i in range(current_row - 1, rows_passed - 1, -1):
            matrix[i][current_column] = counter
            counter += 1
        current_row = i

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()



''' Сложение матриц '''


x = input().split()
n, m = int(x[0]), int(x[1])
matrix1 = [[int(x) for x in input().split()] for _ in range(n)]
z = input()
matrix2 = [[int(x) for x in input().split()] for _ in range(n)]
matrix3 = [[int(x) for x in range(m)] for _ in range(n)]

for i in range(n):
    for q in range(m):
        matrix3[i][q] = matrix1[i][q] + matrix2[i][q]


for i in range(n):
    print(*matrix3[i])




''' Умножение матриц 🌶️ '''


n, m = [int(i) for i in input().split()]
matrix1 = [[int(x) for x in input().split()] for _ in range(n)]
input()
n2, m2 = [int(i) for i in input().split()]
matrix2 = [[int(x) for x in input().split()] for _ in range(n2)]
matrix3 = [[0] * m2 for _ in range(n)]

for i in range(n):
    for q in range(m2):
        for k in range(m):
            matrix3[i][q] += matrix1[i][k] * matrix2[k][q]


for x in matrix3:
    print(*x)



''' Возведение матрицы в степень 🌶️ '''


# Запрашиваем у пользователя размерность матрицы
n = int(input())

# Создаем исходную матрицу, считывая ее с клавиатуры
# Генератор списка считывает строку ввода, разделяет ее по пробелам и конвертирует каждый элемент в int
matrix1 = [[int(x) for x in input().split()] for _ in range(n)]

# Запрашиваем у пользователя степень, в которую будем возводить матрицу
x = int(input())

# Копируем исходную матрицу для дальнейших вычислений
matrix2 = matrix1.copy()

# Производим умножение матриц (возводим в степень)
for _ in range(x - 1):
    # Создаем новую матрицу, заполненную нулями
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for q in range(n):
            for k in range(n):
                matrix[i][q] += matrix1[i][k] * matrix2[k][q]

    # После каждого умножения обновляем матрицы для следующего шага
    matrix1 = matrix2 = matrix

# Выводим окончательную матрицу
for row in matrix1:
    print(*row)



