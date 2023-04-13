minn = float('inf')

for i in range(1, 10_000):
    n = bin(i)[2:]
    n = '1' + n + '0' if i % 2 == 0 else '11' + n + '11'
    if int(n, 2) > 52:
        minn = min(minn, int(n, 2))
print(minn)