file = open('27A.txt')
n = int(file.readline())
nums = [int(i) for i in file]
k = [[] for i in range(80)]
maxx = float('-inf')
for i in nums:
    k[i % 80].append(i)

ns = []
for i in range(len(k)):
    k[i].sort()
    ns += k[i][:5] + k[i][-5:]

for i in range(len(ns)):
    for j in range(i + 1, len(ns)):
        if abs(ns[i] - ns[j]) % 80 == 0:
            maxx = max(maxx, abs(ns[i] - ns[j]))
print(maxx)