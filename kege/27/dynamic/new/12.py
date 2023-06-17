file = open('27A_2753.txt')
n = int(file.readline())
nums = [int(i) for i in file]
count = 0
k = [0] * 8

for i in range(7 + 1):
    for j in range(8):
        if (j + nums[i] % 8) % 8 != 0:
            count += k[j]
    k[nums[i] % 8] += 1
    
for i in range(7 + 1, n):
    k[nums[i - (7 + 1)] % 8] -= 1

    for j in range(8):
        if (j + (nums[i] % 8)) % 8 != 0:
            count += k[j]
    k[nums[i] % 8] += 1
print(count)