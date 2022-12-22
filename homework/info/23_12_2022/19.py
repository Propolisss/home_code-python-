def f(s, count, target):
    if s >= 165: return (count % 2) == (target % 2)
    if count == target: return 0
    h = [f(s + 1, count + 1, target), f(s + 4, count + 1, target), f(s * 2, count + 1, target)]
    return any(h) if (count + 1) % 2 == target % 2 else all(h)

for i in range(1, 164 + 1):
    if f(i, 0, 4):
        print(i)