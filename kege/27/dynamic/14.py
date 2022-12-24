file = open('27A.txt')
n = int(file.readline())
nums = [int(i) for i in file]
k = [float('inf')] * 144
minn = float('inf')

for i in nums:
    ost = 0 if i % 144 == 0 else 144 - i % 144
    if k[ost] < i:
        minn = min(minn, k[ost] + i)
    k[i % 144] = min(k[i % 144], i)
print(minn)