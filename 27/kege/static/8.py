file = open('27B.txt')
n = int(file.readline())
nums = [int(i) for i in file]
k80_50 = [0] * 80
k80 = [0] * 80

for i in nums:
    if i > 50000:
        k80_50[i % 80] += 1
    else:
        k80[i % 80] += 1

count = k80_50[0] * (k80_50[0] - 1) // 2
count += k80_50[40] * (k80_50[40] - 1) // 2
count += k80_50[0] * k80[0]

for i in range(1, 39 + 1):
    count += k80_50[i] * k80_50[80 - i]

for i in range(1, 80):
    count += k80_50[i] * k80[80 - i]
    
print(count)
