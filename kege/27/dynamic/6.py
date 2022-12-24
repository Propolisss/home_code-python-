file = open('27A.txt')
n = int(file.readline())
nums = [int(i) for i in file]
maxx1 = float('-inf')
maxx0 = float('-inf')

for i in nums:
    if i & 1:
        maxx1 = max(maxx1, i)
    else:
        maxx0 = max(maxx0, i)
print(maxx1 + maxx0)