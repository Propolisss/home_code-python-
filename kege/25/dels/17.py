from math import *

def simle(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n > 1

for i in range(ceil(106732567 ** 0.25), int(152673836 ** 0.25) + 1):
    if simle(i):
        print(i ** 4, i ** 3)