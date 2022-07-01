for i in range(10000):
    s = i
    n = 32
    while n > s:
        s = s + 1
        n = n - 1
    if n >= 30:
        print(i)
        break