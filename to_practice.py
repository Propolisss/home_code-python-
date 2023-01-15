pl = 520

maxx = float('-inf')

for x1 in range(0, 100):
    for x2 in range(0, 100):
        temp = x1 * 50 + x2 * 60
        cost = x1 * 1500 + x2 * 1700
        if temp <= pl:
            maxx = max(maxx, cost)
        if cost == 15400:
            print(x1, x2)
print(maxx)