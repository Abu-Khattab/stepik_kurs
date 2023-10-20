''' exemple '''


a = input().split()
c = [[]]

for i in range(len(a)):
    for j in range(len(a) - i):
        b = a[j:j+i+1]
        c.append(b)

print(c)


