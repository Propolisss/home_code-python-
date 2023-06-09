for a in range(-100, 100):
    for b in range(-100, 100):
        for n in range(50):
            x = -7
            y = -1
            for i in range(n):
                x += 15; y += 22
                x += a; y += b
            x += 23; y -= 32
            if x == 1 and y == -3:
                print(a, b, n)