ans = set()

for i in range(1, 1_000_000):
    n = bin(i)[2:]
    n += n[-1]
    for i in range(2):
        if n.count('1') % 2 == 0:
            n += '0'
        else:
            n += '1'
    if int(n, 2) > 144:
        ans.add(int(n, 2))
print(min(ans))