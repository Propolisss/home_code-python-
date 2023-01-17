ans = []

for a in range(1, 10000):
    flag = 0
    for x in range(1, 10000):
        flag += (x % 12 == 0) and (70 <= x <= 80) and (x % a != 0)
        if flag:
            break
    if not flag:
        ans.append(a)
print(len(ans))