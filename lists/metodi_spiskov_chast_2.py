# ''' Все сразу 2 🌶️ '''
#
# numbers = [8, 9, 10, 11]
# del numbers[1]
# numbers.insert(1, 17)  # numbers[1] = 17
# numbers.extend([4, 5, 6])
# del numbers[0]
# numbers += numbers                      # numbers *= 2
# numbers.insert(3,25)
#
# print(numbers)


# ''' меняет местами минимальный и максимальный элемент этого списка. '''
#
# s = input().split()
# s1 = [int(i) for i in s]
# a = s1.index(max(s1))
# b = s1.index(min(s1))
# s1[a], s1[b] = s1[b], s1[a]
# print(*s1)


# ''' или '''
#
# l = [int(i) for i in input().split()]
# x = l.index(min(l))
# y = l.index(max(l))
# l[x], l[y] = max(l), min(l)
# print(*l)


# ''' Количество артиклей '''
#
# s = input().lower().split()
# counter = []
# for i in s:
#     if i == 'a' or i == 'an' or i == 'the':
#         counter.append(i)
# print("Общее количество артиклей:", len(counter))


# ''' или '''
#
# seq = input().lower().split()
# res = seq.count("a") + seq.count("an") + seq.count("the")
#
# print(f"Общее количество артиклей: {res}")


# ''' сортирует и выводит данный список сначала по возрастанию, а затем по убыванию '''
#
# num = [int(i) for i in input().split()]
# num.sort()
# print(*num)
# num.sort(reverse=True)
# print(*num)


# ''' или '''
#
# n = input().split()
# n.sort(key=int)
# print(*n)
# n.sort(reverse=True, key=int)
# print(*n)

# ''' удалить комментарии и символы пустого пространства в конце строк 🌶️ '''
#
# n = input()
# for _ in range(int(n[1:])):
#     s = input()
#     if '#' in s:
#         s = s[:s.find('#')]
#     print(s.rstrip())
#
#
# ''' или '''
#
# n = int(input()[1:])
# for _ in range(n):
#     s = input() + " "
#     print(s[:s.find("#")].rstrip())
#
#
# ''' или '''
#
# n = int(input()[1:])
# for _ in range(n):
#     s = input() + " "
#     print(s[:s.find("#")].rstrip())
#
#
# ''' или '''
#
# n = input().split('#')
# for i in range(int(n[1])):
#     print(input().split('#')[0].rstrip())