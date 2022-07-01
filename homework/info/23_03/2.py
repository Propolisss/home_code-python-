list = []

for a in range(1, 10000):
    flag = 1
    for x in range(1, 10000):
        flag *= (a % 5 == 0) and ((2020 % a != 0) <= ((x % 1718 == 0) <= (2023 % a == 0)))
        if not flag:
            break
    if flag:
        list.append(a)
print(len(list))