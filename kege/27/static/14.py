file = open('27B.txt')
n = int(file.readline())
nums = [int(i) for i in file]
k3 = []
k2 = []
k = []

for i in nums:
    if i % 2 == 0:
        k2.append(i)
    elif i % 3 == 0:
        k3.append(i)
    else:
        k.append(i)

k3.sort()
k2.sort()
k.sort()
nn = k3[-20:] + k2[-20:] + k[-20:]
maxx = float('-inf')

for i in range(len(nn)):
    for j in range(i + 1, len(nn)):
        for k in range(j + 1, len(nn)):
            for l in range(k + 1, len(nn)):
                if (nn[i] * nn[j] * nn[k] * nn[l]) % 12 == 0:
                    maxx = max(maxx, nn[i] + nn[j] + nn[k] + nn[l])
print(maxx)