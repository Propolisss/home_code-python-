file = open('27A_2752.txt')
n = int(file.readline())
nums = [int(i) for i in file]
count = 0
k = [0] * 10

for i in range(5, n):
    x = nums[i]
    if x % 10 == 1: count += k[3]
    if x % 10 == 3: count += k[1]
    if x % 10 == 9: count += k[7]
    if x % 10 == 7: count += k[9]

    if nums[i - 5] % 10 == 1: k[1] += 1
    if nums[i - 5] % 10 == 3: k[3] += 1
    if nums[i - 5] % 10 == 7: k[7] += 1
    if nums[i - 5] % 10 == 9: k[9] += 1
print(count)