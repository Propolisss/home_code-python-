count = 0
d1 = 0
d2 = 0

for i in range(174457, 174506):
    for j in range(2, i):
        if d2 != j:
            if i % j == 0:
                d1 = j
                count += 1
                if count > 2:
                        d1 = 0
                        d2 = 0
                        count = 0
                        break
                if i % d1 == 0:
                    d2 = int(i / d1)
                    count += 1
    if count == 2:
        print(d1, d2)
        d1 = 0
        d2 = 0
        count = 0