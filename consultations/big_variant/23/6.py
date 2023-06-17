def f(start, end, flag):
    if '5' in str(start):
        flag = 0
    if start > end:
        return 0
    elif start == end:
        return flag
    else:
        return f(start + 1, end, flag) + f(start * 2, end, flag)
print(f(1, 60, 1))