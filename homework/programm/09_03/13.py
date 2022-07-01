count = 0
maxx = 0

def fun(n):
    if (n % 8 == 0 or n % 19 == 0) and (n % 4 != 0 and n % 9 != 0 and n % 14 != 0 and n % 16 != 0):
        return True
    else:
        return False

for i in range(8812, 12285 + 1):
    if fun(i):
        count += 1
        maxx = i
print(count, maxx, sep = '')