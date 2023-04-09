def f(start, end):
    if start < end:
        return 0
    elif start == end:
        return 1
    else:
        return f(start - 2, end) + f(start - 5, end)
print(f(23, 2))