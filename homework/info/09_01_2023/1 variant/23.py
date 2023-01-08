

def f(start, end):
    if start > end:
        return 0
    elif start == 12:
        return 0
    elif start == end:
        return 1
    else:
        return f(start + 1, end) + f(start + 3, end)
print(f(7, 27) * f(27, 50))