file = open('27A.txt')
n = int(file.readline())
nums = [int(i) for i in file]
k = [[] * 1 for i in range(11)]

for i in nums:
    k[i % 11].append(i)

nn = []

for i in range(len(k)):
    k[i].sort()
    nn += k[i][:10]

minn = float('inf')
for i in range(len(nn)):
    for j in range(i + 1, len(nn)):
        for k in range(j + 1, len(nn)):
            if (nn[i] + nn[j] + nn[k]) % 11 == 0:
                minn = min(nn[i] + nn[j] + nn[k], minn)
print(minn)
