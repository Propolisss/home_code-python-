for b in range(-100, 100):
    for n in range(100):
        x = 3
        y = -6
        for i in range(n):
            x += 4; y += b
            x += 6; y -= 6
        x -= 53; y += 26
        if x == 0 and y == 0:
            print(b, n)