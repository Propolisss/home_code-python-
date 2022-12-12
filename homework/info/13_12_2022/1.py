# 74
# 37 73
# 71

def f(s, count, target):
    if s % 3 == 0: return 0
    if s >= 151: return (count % 2) == (target % 2)
    if count == target: return 0
    h = []
    if (s + 1) % 3 != 0: h.append(f(s + 1, count + 1, target))
    if (s + 2) % 3 != 0: h.append(f(s + 2, count + 1, target))
    if (s * 2) % 3 != 0: h.append(f(s * 2, count + 1, target))
    return any(h) if (count + 1) % 2 == target % 2 else all(h)

for i in range(1, 149 + 1):
    if f(i, 0, 4):
        print(i)
