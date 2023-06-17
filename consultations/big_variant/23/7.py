ans = set()

def f(start, count):
    if start != 1 and count <= 5:
        ans.add(start)
    elif count > 5:
        return
    f(start + 1, count + 1)
    f(start * 2, count + 1)
f(1, 0)
print(set(range(2, 100)) - ans)