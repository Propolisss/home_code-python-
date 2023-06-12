def f(start, count, target):
    if start <= 10: return count % 2 == target % 2
    if count == target: return 0
    h = [f(start // 3, count + 1, target), f(start - 10, count + 1, target)]
    return any(h) if (count + 1) % 2 == target % 2 else all(h)
# 98
# 43 128
# 20

count = 0
for i in range(11, 10_000):
    if f(i, 0, 3) and not(f(i, 0, 1)):
        print(i)