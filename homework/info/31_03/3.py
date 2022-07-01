list = []

for a in range(10000):
    flag = 1
    for x in range(10000):
        flag *= (x & 25 != 0) <= ((x & 17 == 0) <= (x & a != 0))
        if not flag:
            break
    if flag:
        list.append(a)
print(min(list))