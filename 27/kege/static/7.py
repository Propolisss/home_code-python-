file = open('27A.txt')
n = int(file.readline())
nums = [int(i) for i in file]
ans = [0] * 69

for i in nums:
    ans[i % 69] += 1

count = 0
for i in range(len(ans)):
    count += ans[i] * (ans[i] - 1) // 2
print(count)