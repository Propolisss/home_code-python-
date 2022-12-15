ans = set()

for i in range(20, 600 + 1):
    n = bin(i)[2:-2]
    ans.add(int(n, 2))
print(len(ans))