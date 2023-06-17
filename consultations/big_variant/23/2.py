def f(start, end):
    if start < end or start == 50:
        return 0
    elif start == end:
        return 1
    else:
        if start % 2 == 0:
            return f(start - 5, end) + f(start - 4, end) + f(start // 2, end)
        else:
            return f(start - 5, end) + f(start - 4, end)
print(f(100, 73) * f(73, 22) * f(22, 2))