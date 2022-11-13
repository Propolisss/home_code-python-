from math import *
file = open('27B.txt')
n = int(file.readline())
nums = [int(i) for i in file]
k19 = 0

for i in range(n):
    if nums[i] % 19 == 0:
        k19 += 1

print(factorial(k19) // (factorial(3) * factorial(k19 - 3)))