from fnmatch import *

def div(n):
    dels_ = set()

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            dels_ |= {i, n // i}
    return dels_

for i in range(10 ** 7 + 1):
    if fnmatch(str(i), '3*52?'):
        dels = div(i)
        if len(dels) & 1:
            print(i, max(dels))