ans = set()

def f(start, count):
    if count == 6:
        ans.add(start)
    else:
        f(start + 1, count + 1)
        f(start + 2, count + 1)
        f(start * 2, count + 1)
f(1, 0)
print(sum(1 for j in ans if 34 <= j <= 59))