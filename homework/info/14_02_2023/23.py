def f(start, end, summ, flag):
    if sum(summ) % 11 == 0 and sum(summ) > 0:
        flag = True
    if start > end:
        return 0
    elif start == end and flag:
        return 1
    else:
        return f(start + 2, end, summ[1:] + [start], flag) + f(start * 3, end, summ[1:] + [start], flag) + f(start * 4, end, summ[1:] + [start], flag)

print(f(1, 600, [0, 0, 0], False))