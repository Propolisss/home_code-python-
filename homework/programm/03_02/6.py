count = 0

def simple(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for i in range(2532000, 2532160 + 1):
    if simple(i):
        count += 1
        print(count, i)
    if count == 5:
        break