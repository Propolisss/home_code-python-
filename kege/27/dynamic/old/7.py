file = open('27B.txt')
n = int(file.readline())
nums = [int(i) for i in file]
minn31 = []
minn = []

for i in nums:
    if i % 31 == 0: minn31.append(i)
    else: minn.append(i)
minn31.sort()
minn.sort()
k = minn31[:2] + minn[:2]
miin = float('inf')

for i in range(len(k)):
    for j in range(i + 1, len(k)):
        if (k[i] * k[j]) % 31 == 0:
            miin = min(miin, k[i] * k[j])
print(miin)