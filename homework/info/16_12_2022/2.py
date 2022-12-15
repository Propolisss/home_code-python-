print('z x y f')

for z in range(2):
    for x in range(2):
        for y in range(2):
            f = (x <= z) and (y <= x)
            if f:
                print(z, x, y, f)