print('w y x z')

for w in range(2):
    for y in range(2):
        for x in range(2):
            for z in range(2):
                f = ((w <= y) or (not(y <= z))) and (not x) and (not(x == z))
                if f:
                    print(w, y, x, z)