def f(start, end):
    if start > end:
        return 0
    elif start == end:
        return 1
    else:
        return f(start + 1, end) + f(start * 2, end)
print(f(1, 12) * f(12, 30))