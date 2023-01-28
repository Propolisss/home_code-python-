print('y x z w')

for y in range(2):
    for x in range(2):
        for z in range(2):
            for w in range(2):
                f = (y <= x) or (not((x <= z) and (z <= x))) and (not w)
                if not f:
                    print(y, x, z, w)