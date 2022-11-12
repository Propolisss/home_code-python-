ans = []


for x in range(158):
    num1 = (2 * 1) + (x * 158) + (3 * 158 ** 2) + (7 * 158 ** 3) + (2 * 158 ** 4)
    num2 = (0 * 1) + (9 * 158) + (3 * 158 ** 2) + (x * 158 ** 3) + (1 * 158 ** 4)
    res = num1 + num2

    if res % 73 == 0:
        ans.append(res // 73)
print(sum(ans))