ans = set()
def f(start, count):
    if count > 8:
        return 0
    elif count == 8:
        if 1000 <= start <= 1024:
            ans.add(start)
    else:
        f(start + 1, count + 1)
        f(start + 5, count + 1)
        f(start * 3, count + 1)
f(1, 0)
print(len(ans))