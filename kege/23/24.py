def f(start, end, count1):
    count1 += (start & 1)
    if start > end or count1 > 1:
        return 0
    elif start == end:
        return count1 == 1
    else:
        return f(start + 1, end, count1) + f(start + 2, end, count1) + f(start * 2, end, count1)
print(f(2, 40, 0))