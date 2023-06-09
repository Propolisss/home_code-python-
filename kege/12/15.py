for a in range(-100, 100):
    for b in range(-100, 100):
        for c in range(-100, 100):
            x = 0; y = 0; z = 2
            x += 4; y += 8; z += 10
            for i in range(4):
                x += 2; y -= 4; z -= 5
                x += a; y += b; z += c
            if x == 24 and y == 16 and z == 12:
                print(a, b, c)