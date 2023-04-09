def change(n):
    temp = ''

    for i in str(n):
        if i == '9':
            temp += '9'
        else:
            temp += str(int(i) + 1)
    return int(temp)

def f(start, end):
    if start > end:
        return 0
    elif start == end:
        return 1
    else:
        return f(start + 1, end) + f(change(start), end)
print(f(25, 51))