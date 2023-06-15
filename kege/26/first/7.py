file = open('26_954.txt')
n, k, m = map(int, file.readline().split())
nums = sorted(int(i) for i in file)
summ = 0
while k != 0:
    summ += nums[-1] * 0.2
    del nums[-1]
    k -= 1
while m != 0:
    summ += nums[-1] * 0.1
    del nums[-1]
    m -= 1
print(nums[-1], int(summ))