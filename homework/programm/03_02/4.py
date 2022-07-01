N = 437
summ = 0
suum = 0

def simple(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for j in range(2, 10 + 1):
    N = 437
    summ = 0
    while N > 0:
        summ += N % j
        N //= j
    if simple(summ):
        suum += j
        j += 1
print(suum)