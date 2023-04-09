def f(start, end):
    if start > end:
        return 0
    elif start == end:
        return 1
    else:
        return f(start + 1, end) + f(start * 2, end) + f(start * 2 + 1, end)
print(f(int('100', 2), int('11101', 2)))