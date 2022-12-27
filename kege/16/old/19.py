

def f(n):
    if n <= 1:
        return n
    if n > 1 and (n % 3 == 0):
        return n + f(n // 3)
    if n > 1 and (n % 3 != 0):
        return n + f(n + 3)

for i in range(1, 1_000):
    try:
        if f(i) > 100:
            print(i)
            break
    except:
        ...