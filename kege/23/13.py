def f(start, end):
    if start > end or start == 43:
        return 0
    elif start == end:
        return 1
    else:
        return f(start + 2, end) + f(start + start + 1, end) + f(start + start - 1, end)
print(f(7, 63))