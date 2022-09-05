nums = []

for a in range(1, 3000):
    flag = 1
    for x in range(1, 3000):
        flag *= ((x % 2 == 0) <= (x % 3 != 0)) or ((x + a) >= 100)
        if not flag:
            break
    if flag:
        nums.append(a)
print(min(nums))