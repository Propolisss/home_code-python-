file = open('27B.txt')
n = int(file.readline())
nums = [int(i) for i in file]
k23_1 = []
k23_0 = []
k1 = []
k0 = []

for i in nums:
    if (i % 23 == 0) and (i & 1): k23_1.append(i)
    elif (i % 23 == 0) and (i % 2 == 0): k23_0.append(i)
    elif (i % 2 == 0): k0.append(i)
    else: k1.append(i)
k23_1.sort()
k23_0.sort()
k1.sort()
k0.sort()

k = k23_0[-2:] + k23_1[-2:] + k1[-2:] + k0[-2:]
maxx = float('-inf')
for i in range(len(k)):
    for j in range(i + 1, len(k)):
        if ((k[i] + k[j]) % 2 == 0) and (k[i] % 23 == 0 or k[j] % 23 == 0):
            maxx = max(maxx, k[i] + k[j])
print(maxx)