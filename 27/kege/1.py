# solution a
# file = open('27A.txt')
# n = int(file.readline())
# nums = [int(i) for i in file]
# count = 0
#
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if (nums[i] * nums[j]) % 7 == 0:
#             count += 1
# print(count)

file = open('27B.txt')
n = int(file.readline())
nums = [int(i) for i in file]
k = 0
k7 = 0

for i in range(len(nums)):
    if nums[i] % 7 == 0:
        k7 += 1
    else:
        k += 1

print(k7 * k + (k7 * (k7 - 1) // 2))