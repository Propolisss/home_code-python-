def f(start, end, count):
    count += (start % 2 == 0)
    if start > end:
        return 0
    elif start == end:
        return count == 6
    else:
        return f(start + 1, end, count) + f(start + 3, end, count) + f(start + 5, end, count)
print(f(3, 25, 0))