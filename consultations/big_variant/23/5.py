def f(start, end, prev1, prev2):
    if start > end:
        return 0
    elif start == end:
        return 1
    else:
        if prev1 == prev2 == '+1':
            return f(start * 2, end, '*2', prev1)
        elif prev1 == prev2 == '*2':
            return f(start + 1, end, '+1', prev1)
        else:
            return f(start + 1, end, '+1', prev1) + f(start * 2, end, '*2', prev1)
print(f(1, 16, '', ''))