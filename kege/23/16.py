def f(start, end):
    if start > end:
        return 0
    elif start == end:
        return 1
    else:
        if start & 1:
            return f(start + 1, end)
        else:
            return f(start + 1, end) + f((start * 3) // 2, end)
print(f(1, 20))