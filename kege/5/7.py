ans = set()

for i in range(1, 100_000):
    n = bin(i)[2:]
    n += str(n.count('1') % 2)
    n += str(n.count('1') % 2)
    if int(n, 2) < 80:
        ans.add(int(n, 2))
print(len(ans), ans)