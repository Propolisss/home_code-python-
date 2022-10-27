nums = []


for x in range(1, 22):
    for y in range(13):
        st1 = 5 * 22 ** 0 + x * 22 ** 1 + 3 * 22 ** 2 + 2 * 22 ** 3 + x * 22 ** 4
        st2 = y * 13 ** 0 + 9 * 13 ** 1 + y * 13 ** 2 + 7 * 13 ** 3 + 6 * 13 ** 4
        result = st1 - st2
        if result % 57 == 0:
            nums.append([x + y, result // 57])
print(nums)