file = open('27B_2757.txt')
n = int(file.readline())
nums = [int(i) for i in file]
count = 0
k23 = k = 0

for i in range(8, n):
    x = nums[i]
    if x % 23 == 0:
        count += k
    else:
        count += k23
    if nums[i - 8] % 23 == 0:
        k23 += 1
    k += 1
print(count)