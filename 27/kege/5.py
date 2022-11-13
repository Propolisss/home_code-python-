file = open('27B.txt')
n = int(file.readline())
nums = [int(i) for i in file]

k80 = [0] * 80
b50 = [0] * 80

for i in range(n):
    if nums[i] > 50000:
        k80[nums[i] % 80] += 1
    else:
        b50[nums[i] % 80] += 1

summ = (k80[0] * (k80[0] - 1) // 2) + (k80[40] * (k80[40] - 1) // 2)

for i in range(1, len(k80) // 2):
    summ += k80[i] * k80[80 - i]

summ += (k80[0] * b50[0]) + (k80[40] * b50[40])
for i in range(1, 40):
    summ += k80[i] * b50[80 - i]
    summ += b50[i] * k80[80 - i]
print(summ)

