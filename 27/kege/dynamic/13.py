file = open('27A.txt')
n = int(file.readline())
buffer = [int(file.readline()) for _ in range(5)]
nums = [int(file.readline()) for _ in range(n - 5)]
k = [[0] * 13 for i in range(2)]
count = 0

for i in nums:
    if i % 2 == 0: count += k[0][i % 13] + k[1][i % 13]
    elif i & 1: count += k[0][i % 13]

    k[buffer[0] % 2][buffer[0] % 13] += 1
    buffer.append(i)
    buffer.pop(0)
print(count)