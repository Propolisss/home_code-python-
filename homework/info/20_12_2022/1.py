# 18
# 17
# 28 31

def f(a, b, count, target):
    if (a + b) >= 79: return (count % 2) == (target % 2)
    if count == target: return 0
    h = [f(a + 2, b, count + 1, target), f(a * 2, b, count + 1, target), f(a, b + 2, count + 1, target), f(a, b * 2, count + 1, target)]
    return any(h) if (count + 1) % 2 == target % 2 else all(h)


for s in range(1, 69 + 1):
    if f(9, s, 0, 4):
        print(s)
