for b in range(-100, 100):
    for n in range(1, 100):
        x = -3; y = -5
        for i in range(n):
            x += 2; y += b
            x += 8; y -= 12
        x += 2; y += 3
        if x == 59 and y == 46:
            print(b, n)