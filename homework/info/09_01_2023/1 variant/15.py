ans = []

for a in range(1, 1_000):
    flag = True
    for x in range(1, 1_000):
        flag *= ((x % 45 == 0) and (x % 15 != 0)) <= (x % a != 0)
        if not flag:
            break
    if flag:
        ans.append(a)
print(min(ans))