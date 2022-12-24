file = open('27B.txt')
n = int(file.readline())
nums = [int(i) for i in file]
k7 = 0
k = 0
count = 0

for i in nums:
    if i % 7 == 0:
        count += k
    else:
        count += k7

    if i % 7 == 0:
        k7 += 1
    k += 1
print(count)