file = open('27B.txt')
n = int(file.readline())
buffer = []
nums = [int(file.readline()) for _ in range(n)]
k = [[float('inf')] * 1071 for _ in range(2)]
minn = float('inf')

for i in nums:
    for j in buffer:
        if (i + j) % 2 == 0 and (i + j) % 1071 == 0:
            minn = min(i + j, minn)

    buffer.append(i)
    if len(buffer) > 11:
        buffer.pop(0)

print(minn, minn / 1071)
