list = []

for a1 in range(1, 1000):
    for a2 in range(a1 + 1, 1000):
        flag = 1
        for x in range(1, 1000):
            flag *= (((not(a1 <= x < a2))) <= (not(2 <= x <= 20))) or (15 <= x <= 25)
            if not flag:
                break
        if flag:
            list.append(a2 - a1)
print(sorted(list))