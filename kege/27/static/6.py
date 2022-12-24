file = open('27B.txt')
n = int(file.readline())
nums = [int(i) for i in file]

ans = [0] * 131

for i in nums:
    ans[i % 131] += 1

count = ans[0] * (ans[0] - 1) // 2

for i in range(1, len(ans) // 2 + 1):
    count += ans[i] * ans[131 - i]
print(count)
