list = []

for a in range(1, 1000):
    flag = 1
    for x in range(1, 1000):
        flag *= (not(x % a == 0)) <= ((not(x % 21 == 0)) and (not(x % 35 == 0)))
        if not flag:
            break
    if flag:
        list.append(a)
print(max(list))