ans = set()

for i in range(2, 10_000):
    n = i
    n = n // 3 if n % 3 == 0 else n - 1
    n = n // 5 if n % 5 == 0 else n - 1
    n = n // 11 if n % 11 == 0 else n - 1
    if n == 8:
        ans.add(i)
print(len(ans))