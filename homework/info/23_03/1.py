list = []

for a in range(1000):
    flag = 1
    for x in range(1000):
        for y in range(1000):
            flag *= (2 * y + x != 70) or (x < y) or (a < x)
            if not flag:
                break
    if flag:
        list.append(a)
print(max(list))