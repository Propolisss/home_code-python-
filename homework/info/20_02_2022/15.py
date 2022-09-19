nums = []

for a in range(300):
    flag = 1
    for x in range(1, 300):
        for y in range(1, 300):
            flag *= ((2 * x + 3 * y) != 101) or ((x + y) >= a)
    if flag:
        nums.append(a)
print(max(nums))