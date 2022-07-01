x = 0

for i in range(21, 10000):
    x = i
    a = 3*x + 67
    b = 3*x - 61
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    if a == 64:
        print(i)
        break