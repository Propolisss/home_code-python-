ans = set()
def f(start, count):
    if count > 15:
        return 0
    elif count == 15:
        ans.add(start)
    else:
        f(start * 2, count + 1)
        f(start * 2 + 1, count + 1)
f(1, 0)
print(ans, len(ans))