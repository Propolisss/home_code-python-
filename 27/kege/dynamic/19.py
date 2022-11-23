file = open('27A.txt')
n = int(file.readline())
k6 = [float('inf')] * 23
k3 = [float('inf')] * 23
k2 = [float('inf')] * 23
k = [float('inf')] * 23
buffer = [int(file.readline()) for _ in range(6)]
nums = [int(file.readline()) for _ in range(n - 6)]
minn = float('inf')

for i in nums:
    ost = 0 if i % 23 == 0 else 23 - i % 23

    if i % 6 == 0:
        minn = min(minn, k[ost] + i)
    elif i % 3 == 0:
        minn = min(minn, k2[ost] + i, k6[ost] + i)
    elif i % 2 == 0:
        minn = min(minn, k3[ost] + i, k6[ost] + i)
    else:
        minn = min(minn, k6[ost] + i)

    if buffer[0] % 6 == 0: k6[buffer[0] % 23] = min(k6[buffer[0] % 23], buffer[0])
    if buffer[0] % 3 == 0: k3[buffer[0] % 23] = min(k3[buffer[0] % 23], buffer[0])
    if buffer[0] % 2 == 0: k2[buffer[0] % 23] = min(k2[buffer[0] % 23], buffer[0])
    k[buffer[0] % 23] = min(k[buffer[0] % 23], buffer[0])
    buffer.append(i)
    buffer.pop(0)
print(minn, minn / 23)