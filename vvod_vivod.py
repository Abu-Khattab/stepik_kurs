''' exemple '''

from functools import reduce


evaluate = lambda coeff, x: reduce(lambda s, a: s * x + a, coeff)
print(evaluate(map(int, input().split()), int(input())))