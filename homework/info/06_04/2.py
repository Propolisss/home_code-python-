print('x w y z f')
for x in range(2):
    for w in range(2):
        for y in range(2):
            for z in range(2):
                flag = ((x <= w) or y and (not z)) and ((y <= (not z)) or x and (not w))
                if not flag:
                    print(x, w, y, z, flag)