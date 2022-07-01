count = 0
maxx = 0

def num(n):
    if n % 3 == 0 and n % 7 != 0 and n % 17 != 0 and n % 19 != 0 and n % 27 != 0:
        return True
    else:
        return False

for i in range(1016, 7937 +  1):
    if num(i):
        count += 1
        maxx = i
print(count, maxx, sep = '')