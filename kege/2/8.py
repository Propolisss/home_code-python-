print('y x z w')

for y in range(2):
    for x in range(2):
        for z in range(2):
            for w in range(2):
                f = (not y) and x and ((not z) or w)
                if f:
                    print(y, x, z, w)