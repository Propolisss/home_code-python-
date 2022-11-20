file = open('27A.txt')
n = int(file.readline())
nums = [int(i) for i in file]

k23_1 = []
k23_0 = []
k_1 = []
k_0 = []

for i in nums:
    if (i % 23 == 0) and (i & 1): k23_1.append(i)
    elif (i % 23 == 0) and (i % 2 == 0): k23_0.append(i)
    elif (i & 1): k_1.append(i)
    else: k_0.append(i)

k23_1.sort()
k23_0.sort()
k_1.sort()
k_0.sort()
n = k23_1[-2:] + k23_0[-2:] + k_1[-2:] + k_0[-2:]
maxx = float('-inf')
for i in range(len(n)):
    for j in range(i + 1, len(n)):
        if ((n[i] + n[j]) % 2 == 0) and (n[i] % 23 == 0 or n[j] % 23 == 0):
            maxx = max(n[i] + n[j], maxx)
print(maxx)
