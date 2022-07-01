print('w', 'z', 'x', 'y', 'f')
for w in range(0, 2):
    for z in range(0, 2):
        for x in range(0, 2):
            for y in range(0, 2):
                f = (w == z) or (x and (not y)) or w
                if f == 0:
                    print(w, z, x, y, f)