def f(start, end, count):
    if start > end:
        return 0
    elif start == end:
        return count <= 3
    else:
        return f(start + 2, end, count) + f(start * 3, end, count + 1) + f(start * 5, end, count + 1)
print(f(2, 200, 0))