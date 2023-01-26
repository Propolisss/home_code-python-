def f(start, count):
    if count > 5:
        return 0
    else:
        if count != 0:
            ans.add(start)
        return f(start + 1, count + 1) + f(start * 2, count + 1)

ans = set()
f(1, 0)
print(sorted(ans))