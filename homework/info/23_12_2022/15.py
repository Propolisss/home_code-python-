ans = []

for a in range(1, 10_00):
    flag = 1
    for x in range(1, 10_00):
        flag *= ((x % 6 == 0) <= (x % 10 != 0)) or ((x + a) > 121)
        if not flag:
            break
    if flag:
        ans.append(a)
print(min(ans))