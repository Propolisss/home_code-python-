file = open('27B_2363.txt')
n = int(file.readline())
nums = [int(i) for i in file]
summs = [0] * n
summ = 0
k = [0] * 117
count = 0

for i in range(n):
    summ += nums[i]
    summs[i] = summ

for i in range(4, n):
    n = nums[i]
    summ = summs[i]
    if summ % 117 == 0:
        count += 1

    count += k[summ % 117]

    k[summs[i - 4] % 117] += 1
print(count)