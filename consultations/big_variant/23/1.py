def f(start, end):
    if start > end or start == 12:
        return 0
    elif start == end:
        return 1
    else:
        return f(start + 1, end) + f(start + 2, end) + f(start * 2, end)
print(f(2, 9) * f(9, 17))