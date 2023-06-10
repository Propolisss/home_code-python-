file = open('27a_8483.txt')
n = int(file.readline())
k = int(file.readline())
maxx = float('-inf')
nums = [int(i) for i in file]

# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         for l in range(j + 1, len(nums)):
#             if (j - i) >= k and (l - j) >= k:
#                 maxx = max(maxx, nums[i] + nums[j] + nums[l])
# print(maxx)

maxx_num1 = float('-inf')
file.close()
filee = open('27a_8483.txt')
n1 = int(filee.readline())
n1 = int(filee.readline())
rev = nums[::-1]
count = 0
dic = dict()
temp = float('-inf')
c = 0
for i in range(n - k - 1, k - 1, -1):
    temp = max(temp, rev[c])
    dic[i] = temp
    c += 1


for i in range(n):
    num = int(filee.readline())
    if i < k or i > n - k - 1:
        continue
    if i % 500 == 0:
        print(n - i, i)
    count += 1
    #print(nums[i - k], num, rev[n - 2 * k - count])
    maxx_num1 = max(maxx_num1, nums[i - k])
    maxx = max(maxx, num + maxx_num1 + dic[i])
print(maxx)