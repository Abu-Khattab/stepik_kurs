''' Decimal'''


from decimal import *

s = ('0.77 4.03 9.06 3.80 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 '
     '1.46 5.26 4.83 7.23 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78'
     ' 5.37 0.03 9.60 8.86 2.73 5.83 6.50')
num = [Decimal(i) for i in s.split()]
maximum = max(num)
minimum = min(num)
print(minimum + maximum)


''' or '''

from decimal import Decimal as Dcm

s = ('0.77 4.03 9.06 3.80 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 '
     '1.46 5.26 4.83 7.23 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78'
     ' 5.37 0.03 9.60 8.86 2.73 5.83 6.50')
print(Dcm(max(s.split(), key=Dcm)) + Dcm(min(s.split(), key=Dcm)))


''' next task '''

from decimal import *



s = ('9.73 8.84 8.92 9.60 9.32 8.97 8.53 1.26 6.62 9.85 1.85 1.80 0.83 6.75 9.74 9.11 9.14 5.03 5.03 1.34 3.52 8.09 '
     '7.89 8.24 8.23 5.22 0.30 2.59 1.25 6.24 2.14 7.54 5.72 2.75 2.32 2.69 9.32 8.11 4.53 0.80 0.08 9.36 5.22'
     '.08 3.86 5.56 1.43 8.36 6.29 5.13')

num = [Decimal(i) for i in s.split()]

print(sum(num))
print(*sorted(num, reverse=True)[:5])


''' or '''


from decimal import Decimal

s = ('9.73 8.84 8.92 9.60 9.32 8.97 8.53 1.26 6.62 9.85 1.85 1.80 0.83 6.75 9.74 9.11 9.14 5.03 5.03 1.34 3.52 8.09'
     ' 7.89 8.24 8.23 5.22 0.30 2.59 1.25 6.24 2.14 7.54 5.72 2.75 2.32 2.69 9.32 8.11 4.53 0.80 0.08 9.36 5.22 '
     '4.08 3.86 5.56 1.43 8.36 6.29 5.13')

s_decimals = sorted(map(Decimal, s.split()), reverse=True)
print(sum(s_decimals))
print(*s_decimals[:5])


''' next task'''

from decimal import Decimal

num = Decimal(input())
new_num = str(num).split('.')

# Получаем кортеж из цифр Decimal числа
num_tuple = num.as_tuple().digits


# Находим наибольшую и наименьшую цифры
max_digit = max(num_tuple)
min_digit = min(num_tuple)
if new_num[0] == '0' or new_num[0] == '-0':
    min_digit = 0


# Выводим результат
print(f"Сумма наибольшей и наименьшей цифры: {max_digit + min_digit}")



''' or '''

from decimal import *
num = Decimal(input())
mx, mn = max(num.as_tuple().digits), min(num.as_tuple().digits)
print(mx if '0' in str(num) else mx + mn)



''' next task '''


from decimal import *

num = Decimal(input())

res = num.exp() + num.ln() + num.log10() + num.sqrt()
print(res)



''' next task '''

from fractions import Fraction

numbers = ['6.34', '4.08', '3.04', '7.49', '4.45', '5.39', '7.82', '2.76', '0.71', '1.97', '2.54', '3.67', '0.14',
           '4.29', '1.84', '4.07', '7.26', '9.37', '8.11', '4.30', '7.16', '2.46', '1.27', '0.29', '5.12', '4.02',
           '6.95', '1.62', '2.26', '0.45', '6.91', '7.39', '0.52', '1.88', '8.38', '0.75', '0.32', '4.81', '3.31',
           '4.63', '7.84', '2.25', '1.10', '3.35', '2.05', '7.87', '2.40', '1.20', '2.58', '2.46']


for i in numbers:
    v = Fraction(i)
    print(i, '=', v)


''' or '''

from fractions import Fraction

numbers = ['6.34', '4.08', '3.04', '7.49', '4.45', '5.39', '7.82', '2.76', '0.71', '1.97', '2.54', '3.67', '0.14',
           '4.29', '1.84', '4.07', '7.26', '9.37', '8.11', '4.30', '7.16', '2.46', '1.27', '0.29', '5.12', '4.02',
           '6.95', '1.62', '2.26', '0.45', '6.91', '7.39', '0.52', '1.88', '8.38', '0.75', '0.32', '4.81', '3.31',
           '4.63', '7.84', '2.25', '1.10', '3.35', '2.05', '7.87', '2.40', '1.20', '2.58', '2.46']

for num in numbers:
    print(f'{num} = {Fraction(num)}')


''' or '''

from fractions import Fraction as F

numbers = ['6.34', '4.08', '3.04', '7.49', '4.45', '5.39', '7.82',
           '2.76', '0.71', '1.97', '2.54', '3.67', '0.14', '4.29',
           '1.84', '4.07', '7.26', '9.37', '8.11', '4.30', '7.16',
           '2.46', '1.27', '0.29', '5.12', '4.02', '6.95', '1.62',
           '2.26', '0.45', '6.91', '7.39', '0.52', '1.88', '8.38',
           '0.75', '0.32', '4.81', '3.31', '4.63', '7.84', '2.25',
           '1.10', '3.35', '2.05', '7.87', '2.40', '1.20', '2.58', '2.46']

[print(f'{i} = {F(i)}') for i in numbers]


''' next task '''

from fractions import Fraction

s = ('0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 '
     '1.46 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 '
     '37 0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021')

numbers = [Fraction(num) for num in s.split()]

print(max(numbers) + min(numbers))


''' or '''


s = ('0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 '
     '1.46 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 '
     '5.37 0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021')

n = [float(i) for i in s.split()]
digits = list(map(float, n))
mn = min(digits, default=0)
mx = max(digits, default=0)
digit_sum = mn + mx
faction_sum = Fraction(digit_sum).limit_denominator()
print(faction_sum)


''' or '''

from fractions import Fraction

s = list(map(Fraction, '0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63'
                       '8.36 1.56 6.67 1.46 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 '
                       '7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021'.split()))

print(max(s) + min(s))



''' or '''

from fractions import Fraction

s = ('0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 '
     '1.46 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37'
     ' 0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021')
print(Fraction(max(s.split()))+Fraction(min(s.split())))


''' next task '''

from fractions import Fraction as F

print(F(int(input()), int(input())))


''' next task '''


from fractions import Fraction

x, y = input(), input()
for op in '+-*/':
    print(f'{x} {op} {y} = {eval(f"Fraction(x){op}Fraction(y)")}')



''' or '''

from fractions import Fraction


ch = input()
zn = input()

sum_fraction = Fraction(ch) + Fraction(zn)
min_fraction = Fraction(ch) - Fraction(zn)
umn_fraction = Fraction(ch) * Fraction(zn)
raz_fraction = Fraction(ch) / Fraction(zn)
print(f'{ch} + {zn} = {sum_fraction}')
print(f'{ch} - {zn} = {min_fraction}')
print(f'{ch} * {zn} = {umn_fraction}')
print(f'{ch} / {zn} = {raz_fraction}')


''' or '''


from fractions import Fraction as F

a, b = input(), input()

[print(f'{a} {i} {b} = {eval(f"F(a){i}F(b)")}') for i in '+-*/']


''' next task '''


from fractions import Fraction


num1 = int(input())
res = 0
for i in range(1, num1 + 1):
    res += Fraction(1, int(i)**2)


print(res)


''' or '''


from fractions import Fraction as F

print(sum([F(1, i**2) for i in range(1, int(input()) + 1)]))


''' next task '''


from fractions import Fraction
from math import factorial


num1 = int(input())
res = 0
for i in range(1, num1 + 1):
    res += Fraction(1, factorial(i))


print(res)


''' or '''


from fractions import Fraction as F
from math import factorial as f


print(sum(F(1 / F(f(i))) for i in range(1, int(input()) + 1)))



''' Юный математик 🌶️ '''


from fractions import Fraction

n = int(input())

if n % 2 == 0 and (n // 2) % 2 != 0:
    denominator = n // 2 + 2
else:
    denominator = n // 2 + 1

numerator = n - denominator
result_fraction = Fraction(numerator, denominator)
print(result_fraction)


''' or '''


from math import gcd
n = int(input())
a = n // 2
while gcd(a, n - a) != 1:
    a -= 1
print('{}/{}'.format(a, n - a))


''' Упорядоченные дроби '''

from fractions import Fraction as f

n = int(input())
fracs = set()

for i in range(1, n + 1):
    for j in range(1, i):
        fr = f(j, i)
        fracs.add(fr)

for frac in sorted(fracs):
    print(frac)


''' or '''

from fractions import Fraction

numbers = set()

for i in range(2, int(input()) + 1):
    for j in range(1, i):
        numbers.add(Fraction(j, i))

print(*sorted(numbers), sep='\n')



''' complex '''

z = complex(input())
z1 = complex(input())

print(z, '+', z1, '=', z + z1)
print(z, '-', z1, '=', z - z1)
print(z, '*', z1, '=', z * z1)



''' next task '''

numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j, 3 - 2j, -9 + 9j, -1 - 1j,
           -1 - 10j, -20 + 15j, -21 + 1j, 1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]

# Находим комплексное число с наибольшим модулем
max_complex = max(numbers, key=abs)

# Выводим комплексное число и его модуль
print(max_complex)
print(abs(max_complex))


''' next task '''


n = int(input())
z1 = complex(input())
z2 = complex(input())



a = z1.conjugate()
b = z2.conjugate()
print(z1 ** n + z2 ** n + a ** n + b ** (n + 1))


