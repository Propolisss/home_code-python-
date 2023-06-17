file = open('27B_2908.txt')
n = int(file.readline())
nums = [int(i) for i in file]
summs = [[float('inf'), 0] for i in range(n)]
k = [float('inf')] * 7
summ = 0
k7 = 0
maxx = float('-inf')

for i in range(n):
    summ += nums[i]
    if nums[i] % 7 == 0 and nums[i] > 0:
        k7 += 1
    summs[i] = [summ, k7]

for i in range(6, n):
    summ = summs[i][0]
    k7 = summs[i][1]

    if k7 % 7 == 0:
        maxx = max(maxx, summ)
    s1 = summ - k[k7 % 7]
    maxx = max(maxx, s1)

    if summs[i - 6][0] < k[summs[i - 6][1] % 7]:
        k[summs[i - 6][1] % 7] = summs[i - 6][0]
print(maxx)