def f(start, end):
    if start > end or start == 6:
        return 0
    elif start == end:
        return 1
    else:
        return f(start + 2, end) + f(start * 3, end)
print(f(1, 25) * f(25, 63))