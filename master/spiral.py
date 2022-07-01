nums = [[0] * 10000 for i in range(10000)]
orient = 0
i = 1
j = 0
count = 4
nums[0][0] = 1
nums[0][1] = 2
nums[1][1] = 3
nums[1][0] = 4
while count != 10000 * 10000:
    if i == 0:
        j += 1
        while i <= j:
            count += 1
            nums[i][j] = count
            i += 1
        i -= 1
    if j == 0:
        i += 1
        while i >= j:
            count += 1
            nums[i][j] = count
            j += 1
        j -= 1
    if i == j:
        orient += 1
        if orient & 1:
            while i != 0:
                i -= 1
                count += 1
                nums[i][j] = count
        else:
            while j != 0:
                j -= 1
                count += 1
                nums[i][j] = count

print(nums)
"""
n = int(input())

for i in range(n):
    y, x, = map(int, input().split())
    print(nums[y][x])
"""
print(nums[170550340][943050741])