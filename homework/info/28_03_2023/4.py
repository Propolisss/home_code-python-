def simple(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def div(n):
    dels_ = set()

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if simple(i):
                dels_.add(i)
            if simple(n // i):
                dels_.add(n // i)
    return dels_

count = 0

for i in range(500_000 - 1, -1, -1):
    dels = div(i)
    if len(dels) != 0 and sum(dels) % 10 == 0:
        print(i, sum(dels))
        count += 1
    if count == 7:
        break