minn = float('inf')

for i in range(1, 10_000):
    n = bin(i)[2:]
    n += str(n.count('1') % 2)
    n += str(n.count('1') % 2)
    if int(n, 2) > 80:
        minn = min(minn, int(n, 2))
print(minn)