from math import *
count = 0

for i in range(1, 16, 2):
    count += (factorial(16)) // (factorial(i) * (factorial(16 - i)))
print(count)