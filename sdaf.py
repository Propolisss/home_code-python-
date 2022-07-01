def simple(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

sums = []

for i in range(3000000 // 6, (10000000 // 6) + 1):
    n1 = 6 * i + 1
    n2 = 6 * i - 1
    sr = (n1 + n2) // 2
    if simple(n1) and simple(n2):
        sums.append(sr)
print(len(sums), sums[-1])