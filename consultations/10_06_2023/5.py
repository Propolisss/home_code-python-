ans = set()


for i in range(30_000_000):
    n = bin(i)[2:]
    if i % 5 == 0:
        n = n[:3] + n
    else:
        n = n + bin((i % 3) * 5)[2:]
    if int(n, 2) > 39000:
        ans.add(int(n, 2))
print(min(ans))