file = open('27A.txt')
n = int(file.readline())
buffer = []
nums = [int(file.readline()) for _ in range(n)]
count = 0
for i in nums:
    for j in range(len(buffer)):
        if (i + buffer[j]) % 8 != 0:
            count += 1
    buffer.append(i)
    if len(buffer) > 7:
        buffer.pop(0)
print(count)