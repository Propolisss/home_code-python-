for a in range(-100, 100):
    for b in range(-100, 100):
        x = -5; y = 15
        for i in range(4):
            x += 5; y += 1
            x += a; y += b
        x += 90; y += 4
        if x == 5 and y == 3:
            print(a, b)