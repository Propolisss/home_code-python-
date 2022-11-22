file = open('27A.txt')
n = int(file.readline())
buffer = [int(file.readline()) for i in range(8)]
nums = [int(file.readline()) for _ in range(n - 8)]
k23 = 0
k = 0
count = 0

for i in nums:
    if i % 23 == 0:
        count += k
    else:
        count += k23

    k += 1
    if buffer[0] % 23 == 0: k23 += 1
    buffer.append(i)
    buffer.pop(0)
print(count)