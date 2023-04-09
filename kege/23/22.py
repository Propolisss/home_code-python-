def f(start, end, count2):
    if start > end:
        return 0
    elif start == end:
        return count2 == 1
    else:
        return f(start + 1, end, count2) + f(start + 2, end, count2) + f(start * 2, end, count2 + 1)
print(f(2, 12, 0))