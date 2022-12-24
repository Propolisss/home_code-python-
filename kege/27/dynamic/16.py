file = open('27B.txt')
n = int(file.readline())
nums = [int(i) for i in file]
k = [float('-inf')] * 101
maxx = float('-inf')

for i in nums:
    if i % 100 > 12:
        ost = 112 - i % 100
    else:
        ost = 12 - i % 100
    if k[ost] != float('-inf'):
        if k[ost] > i:
            maxx = max(maxx, k[ost] + i)
    if i % 100 > 12:
        k[i % 100] = max(k[i % 100], i)
    else:
        k[i % 100] = max(k[i % 100], i)
print(maxx)