minn = float('inf')

for i in range(1, 10_000):
    n = bin(i)[2:]
    n += n[-1]
    n += str(int(n.count('1') & 1))
    n += str(int(n.count('1') & 1))
    if int(n, 2) > 144:
        minn = min(minn, int(n, 2))
print(minn)