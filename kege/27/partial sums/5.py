file = open('27B_2481.txt')
n = int(file.readline())
nums = []

for i in range(n):
    x = int(file.readline())
    nums += [x] + [a + x for a in nums]
    nums = list({j % 17 : j for j in sorted(nums)}.values())
print(max(i for i in nums if i % 17 == 0))