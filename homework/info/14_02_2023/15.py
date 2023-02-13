def od(n, m):
    n_ = set()
    m_ = set()

    for i in range(1, int(n ** 0.5) + 1):
        if i == 1:
            n_.add(n // i)
        else:
            if n % i == 0:
                n_ |= {i, n // i}

    for i in range(1, int(m ** 0.5) + 1):
        if i == 1:
            m_.add(m // i)
        else:
            if m % i == 0:
                m_ |= {i, m // i}
    if any(i in m_ for i in n_):
        return True
    return False

def f(x):
    return (od(x, 42)) <= (not(od(x, 7))) or (x + a >= 25)

for a in range(1, 1000):
    if all(f(x) for x in range(3000)):
        print(a)
        break