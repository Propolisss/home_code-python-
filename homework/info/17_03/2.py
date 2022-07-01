list = []

for a1 in range(1, 1000):
    for a2 in range(a1 + 1, 1000):
        flag = 1
        for x in range(1000):
            flag *= ((20 <= x <= 50) <= (a1 <= x < a2)) and ((a1 <= x < a2) <= (10 <= x <= 60))
            if not flag:
                break
        if flag:
            print(a1, a2)