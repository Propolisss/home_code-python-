def f(start, end):
    if start < end:
        return 0
    elif start == end:
        return 1
    else:
        return f(start - 1, end) + f(start - 3, end) + f(start // 3, end)
print(f(22, 2))