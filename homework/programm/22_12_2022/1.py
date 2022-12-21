def div(n):
    dels_ = set()

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            dels_ |= {i, n // i}
    return dels_


ans = []
for i in range(30_000, 50_000 + 1):
    dels = div(i)
    count = 0

    for j in dels:
        if j in [3, 5, 11, 13]:
            count += 1
    if count == 3:
        ans.append(i)
print(len(ans), max(ans))