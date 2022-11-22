file = open('27A.txt')
n = int(file.readline())
buffer = [int(file.readline()) for _ in range(5)]
nums = [int(file.readline()) for _ in range(n - 5)]
k = [0] * 10
count = 0

for i in nums:
    if i % 10 == 1: count += k[3]
    elif i % 10 == 3: count += k[1]
    elif i % 10 == 9: count += k[7]
    elif i % 10 == 7: count += k[9]

    k[buffer[0] % 10] += 1
    buffer.append(i)
    buffer.pop(0)
print(count)