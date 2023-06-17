file = open('27B_2756.txt')
n = int(file.readline())
nums = [int(i) for i in file]
k = [float('-inf')] * 100
maxx = float('-inf')

for i in range(n):
    x = nums[i]
    ost = (12 - x % 100) % 100 if x % 100 <= 12 else (112 - x % 100) % 100
    if k[ost] > x:
        maxx = max(maxx, k[ost] + x)

    k[x % 100] = max(k[x % 100], x)
print(maxx)