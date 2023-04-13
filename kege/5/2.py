minn = float('inf')

for i in range(1, 10_000):
    n = bin(i)[2:]
    n += '01' if i % 2 == 0 else '10'
    if int(n, 2) > 81:
        minn = min(minn, int(n, 2))
print(minn)