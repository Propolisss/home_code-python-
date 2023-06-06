def f(start, end, arr, flag):
    if sum(arr) % 11 == 0:
        flag = 1
    if start > end:
        return 0
    elif start == end:
        return flag == 1
    else:
        return f(start + 2, end, arr[1:] + [start], flag) + f(start * 3, end, arr[1:] + [start], flag) + f(start * 4, end, arr[1:] + [start], flag)

print(f(1, 600, [0, 0, 1], 0))