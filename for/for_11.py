n = int(input())
sum1 = 0
sum2 = 0

for i in range(1, n):
    sum1 += int(input())

for j in range(1, n + 1):
    sum2 += j

print(abs(sum1 - sum2))