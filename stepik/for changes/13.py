
def div(n):
    dels = set()

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if sum(int(k) for k in str(i)) == 20:
                dels.add(i)
            if sum(int(k) for k in str(n // i)) == 20:
                dels.add(n // i)
    return sorted(dels)



count = 0
for i in range(400_000_000, 500_000_000):
    dels = div(i)
    if len(dels) >= 6:
        print(dels[-6], len(dels))
        count += 1
    if count == 5:
        break