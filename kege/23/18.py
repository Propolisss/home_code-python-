def f(start, end, count):
    if start > end or count > 7:
        return 0
    elif start == end:
        return count == 7
    else:
        return f(start + 1, end, count + 1) + f(start + 4, end, count + 1) + f(start * 2, end, count + 1)
print(f(3, 27, 0))