print('x y z')

for x in range(2):
    for y in range(2):
        for z in range(2):
            f = not(x == (y <= z))
            print(x, y, z, f)