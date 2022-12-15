ans = []

for a in range(0, 1_000):
    flag = 1
    for x in range(0, 1_000):
        for y in range(0, 1_000):
            flag *= ((2 * x + y) != 70) or (x < y) or (a < x)
            if not flag:
                break
        if not flag:
            break
    if flag:
        ans.append(a)
print(max(ans))