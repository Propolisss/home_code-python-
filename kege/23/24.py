def f(start, end, count):
    if start > end:
        return 0
    elif start == end:
        return count == 6
    else:
        return f(start + 1, end, count + (start % 2 == 0)) + f(start + 3, end, count + (start % 2 == 0)) + f(start + 5, end, count + (start % 2 == 0))
print(f(3, 25, 0))