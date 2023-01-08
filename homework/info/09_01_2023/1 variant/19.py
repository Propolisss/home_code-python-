def f1(s, count, target):
    if s == 1: return (count % 2) == (target % 2)
    if count == target: return 0
    h = []
    if (s % 6 == 0):
        h.append(f1(s // 2, count + 1, target))
        h.append(f1(s // 3, count + 1, target))
    elif (s % 2 == 0):
        h.append(f1(s - 3, count + 1, target))
        h.append(f1(s // 2, count + 1, target))
    elif (s % 3 == 0):
        h.append(f1(s // 3, count + 1, target))
        h.append(f1(s - 2, count + 1, target))
    else:
        h.append(f1(s - 3, count + 1, target))
        h.append(f1(s - 2, count + 1, target))
    return any(h) if (count + 1) % 2 == target % 2 else all(h)


for i in range(2, 37 + 1):
    for k in range(1, 10):
        if f1(i, 0, k):
            print(i, k)
