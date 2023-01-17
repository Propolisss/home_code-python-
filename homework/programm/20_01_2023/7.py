ans = []

for a in range(1, 1000):
    flag = 1
    for x in range(1, 1000):
        flag *= ((x % 2 == 0) <= (x % 3 != 0)) or (x + a >= 80)
        if not flag:
            break
    if flag:
        ans.append(a)
print(min(ans))