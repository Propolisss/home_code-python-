list = []

for a in range(1, 10000):
    flag = 1
    for x in range(1, 10000):
        flag *= ((x % 84 != 0) or (x % 90 != 0)) <= (x % a != 0)
        if not flag:
            break
    if flag:
        list.append(a)
print(min(list))