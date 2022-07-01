count = 0
maxx = 0

def num(n):
    if (n % 4 == 0 or n % 5 == 0) and n % 9 != 0 and n % 11 != 0 and n % 17 != 0 and n % 23 != 0:
        return True
    return False

for i in range(3361, 9205 + 1):
    if num(i):
        count += 1
        maxx = i
print(count, maxx, sep = '')