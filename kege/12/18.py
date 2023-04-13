def f(start, end, count):
    if start > end:
        return 0
    elif start == end:
        return count == 4
    else:
        summ = 0
        for i in range(1, 10):
            summ += f(start + i, end, count + 1)
        return summ
print(f(0, 5, 0))