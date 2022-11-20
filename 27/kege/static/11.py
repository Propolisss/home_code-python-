file = open('27B.txt')
n = int(file.readline())
nums = [int(i) for i in file]
minn31 = float('inf')
minn = float('inf')

for i in nums:
    if i % 31 == 0:
        minn31 = min(minn31, i)
    else:
        minn = min(minn, i)
print(minn31 * minn)

