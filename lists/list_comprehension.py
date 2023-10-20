# ''' создать список состоящий из 10 нулей '''
#
# zeros = []
# for i in range(10):
#     zeros.append(0)
# print(zeros)
#
#
# ''' списка целых чисел от 0 до 9'''
#
# numbers = []
# for i in range(10):
#     numbers.append(i)


# ''' списка целых чисел от 0 до 9'''
#
# numbers = [i for i in range(10)]
# print(numbers)


# ''' список четных чисел от 0 до 20 '''
#
# evens = [i for i in range(21) if i % 2 == 0]
# print(evens)
#
#
# ''' Создать список, заполненный кубами целых чисел от 10 до 20 '''
#
# cubes = [i ** 3 for i in range(10, 21)]
#
#
# ''' список, заполненный символами строки '''
#
# chars = [c for c in 'abcdefg']
# print(chars)


# ''' Такой код равнозначен следующему: '''
#
# numbers = []
#
# for i in range(1, 5):
#     for j in range(2):
#         numbers.append(i * j)
# print(numbers)
#
# ''' вложенные циклы. '''
#
# numbers = [i * j for i in range(1, 5) for j in range(2)]
# print(numbers)


# ''' получить новый список, содержащий строки исходного списка с удаленным первым символом. '''
#
#
# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif',
#             'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
#             'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
#
# new_keywords = [i[1:] for i in keywords]
#
# print(new_keywords)




# ''' новый список, содержащий длины строк исходного списка. '''
#
# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del',
# 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
# 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
#
# lengths = [len(i) for i in keywords]
#
# print(lengths)



# ''' новый список, содержащий только слова длиной не менее пяти символов (включительно). '''
#
# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif',
#             'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
#             'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
#
# new_keywords = [i for i in keywords if len(i) > 4]
#
# print(new_keywords)


# ''' список всех чисел-палиндромов от 100 до 1000 '''
#
# palindromes = [i for i in range(100, 1001) if str(i)[0] == str(i)[-1]]
#
# print(palindromes)



# ''' создает список, содержащий квадраты чисел от 1 до n '''
#
# lines = [i ** 2 for i in range(1, int(input()) + 1)]
# print(*lines, sep='\n')


# ''' кубы указанных чисел также на одной строке '''
#
# cub = [int(i) ** 3 for i in input().split()]
# print(*cub)


# ''' выводит слова введенной строки в столбик. '''
#
# word = [i for i in input().split()]
# print(*word, sep='\n')


# ''' выводит все цифровые символы данной строки. '''
#
# word = [i for i in input() if i in '0123456789']
# print(*word, sep='')



# ''' выводит не оканчивающиеся на цифру 4 квадраты четных чисел'''
#
# chars = [int(i) ** 2 for i in input().split() if int(i) ** 2 % 10 != 4 and int(i) % 2 == 0]
# print(*chars)

