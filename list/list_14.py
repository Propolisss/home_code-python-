list = input().split()
l = []

for i in range(len(list)):
    if list.count(list[i]) == 1:
        l.append(list[i])
print(' '.join(l))