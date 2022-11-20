file = open('27A.txt')
n = int(file.readline())
nums = [int(i) for i in file]
n1 = []
n0 = []

for i in nums:
    if i & 1:
        n1.append(i)
    else:
        n0.append(i)
n1.sort()
n0.sort()
n = n1[-2:] + n0[-2:]
maxx = float('-inf')

for i in range(len(n)):
    for j in range(i + 1, len(n)):
        if (n[i] + n[j]) & 1:
            maxx = max(n[i] + n[j], maxx)
print(maxx)