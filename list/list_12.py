list = [int(i) for i in input().split()]
k, c = [int(i) for i in input().split()]
list.append(c)
n = 0

while list[k] != c:
    n += 1
    list[len(list) - n], list[len(list) - (n + 1)] = list[len(list) - (n + 1)], list[len(list) - n]
print(' '.join(str(i) for i in list))