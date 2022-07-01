list = input().split()
l = []
count = 0

for i in range(len(list)):
    if list[i] not in l:
        l.append(list[i])
print(len(l))