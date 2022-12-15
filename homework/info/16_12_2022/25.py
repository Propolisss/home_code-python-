def div(n):
    dels_ = set()

    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            if (i & 1):
                dels_.add(i)
            else:
                return {0}
            if ((n // i) & 1):
                dels_.add(n // i)
            else:
                return {0}
    return dels_


for i in range(321654, 654321 + 1):
    dels = div(i)
    if len(dels) > 70:
        print(i, max(dels))