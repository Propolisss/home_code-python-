file = open('26_2653.txt')
n = int(file.readline())
nums = sorted(int(i) for i in file)
ans = set()

for i in nums:
    ans |= {j + i for j in ans} | {i}
girs = set(range(1, sum(nums) + 1)) - ans
print(len(girs), max(girs))

# nums = sorted(int(i) for i in file)
# weight = [0] * (sum(nums) + 1)
# summ = 0
#
# for i in nums:
#     weight2 = weight.copy()
#     summ += i
#     for j in range(summ + 1):
#         if weight[j] > 0:
#             weight2[j + i] += weight[j]
#     weight2[i] += 1
#     weight = weight2
#
# count = 0
# maxx = float('-inf')
# for i in range(1, len(weight)):
#     if weight[i] == 0:
#         count += 1
#         maxx = max(maxx, i)
# print(count, maxx)