print('x y z f')

for x in range(2):
    for y in range(2):
        for z in range(2):
            f = ((not x) and y and z) or ((not x) and (not z))
            if f:
                print(x, y, z, f)