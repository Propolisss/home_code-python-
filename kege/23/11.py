def f(start, end):
    if start > end or start == 11 or start == 18:
        return 0
    elif start == end:
        return 1
    else:
        return f(start + 1, end) + f(start + 2, end) + f(start * 3, end)
print(f(4, 8) * f(8, 23))