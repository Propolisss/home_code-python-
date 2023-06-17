file = open('27A.txt')
n = int(file.readline())
buffer = [int(file.readline()) for _ in range(4)]
nums = [int(file.readline()) for _ in range(n - 4)]
k = [[float('inf'), float('-inf')] for i in range(137)]
maxx = float('-inf')

for i in nums:
    if k[i % 137][0] != float('inf'):
        maxx = max(maxx, abs(k[i % 137][0] - i))
    if k[i % 137][1] != float('-inf'):
        maxx = max(maxx, abs(k[i % 137][1] - i))

    k[buffer[0] % 137][0] = min(k[buffer[0] % 137][0], buffer[0])
    k[buffer[0] % 137][1] = max(k[buffer[0] % 137][1], buffer[0])

    buffer.append(i)
    buffer.pop(0)
print(maxx)

