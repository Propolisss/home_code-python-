def f(start, end, last):
    if start > end:
        return 0
    elif start == end:
        return 1
    else:
        if last == '*2':
            return f(start + 1, end, '+1') + f(start + 2, end, '+2')
        else:
            return f(start + 1, end, '+1') + f(start + 2, end, '+2') + f(start * 2, end, '*2')
print(f(1, 15, ''))