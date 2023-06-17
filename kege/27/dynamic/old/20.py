file = open('27A.txt')
n = int(file.readline())
# buffer = []
# nums = [int(i) for i in file]
# minn = float('inf')
# k = [float('inf')] * 107
#
# for i in range(len(nums)):
#     for j in range(i + 5, len(nums), 5):
#         if abs(i - j) % 5 == 0:
#             if (nums[i] + nums[j]) % 107 == 0:
#                 minn = min(minn, nums[i] + nums[j])
# print(minn, minn / 107)
k = [[float('inf')] * 107 for i in range(5)]
minn = float('inf')

for i in range(n):
    x = int(file.readline())
    ind = i % 5
    ost = 0 if x % 107 == 0 else 107 - x % 107

    if k[ind][ost] != float('inf'):
        minn = min(minn, k[ind][ost] + x)

    k[ind][x % 107] = min(k[ind][x % 107], x)
print(minn)