file =open('27B_2759.txt')
n = int(file.readline())
nums = [int(i) for i in file]
m = [0] * 135
count = 0

for i in range(len(nums)):
    if nums[i] <= 134:
        for j in range(nums[i] + 1, 134 + 1):
            if nums[i] + j <= 134:
                count += m[j]
        m[nums[i]] += 1
print(count)