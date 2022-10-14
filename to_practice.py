delt = []
nums = []


def f(start, end, count, current):
    global nums
    global delt
    nums.append(current)
    delt.append(nums[:])
    for i in range(1, len(delt[-1])):
        if delt[-1][i - 1] == 2 and delt[-1][i] == 2:
            del delt[-1]
            nums.clear()
            return 0
    if start > end:
        return 0
    if start == end:
        return 1
    else:
        return f(start * 3, end, count + 1, 2) + f(start + 1, end, count + 1, 1) + f(start + 2, end, count + 1, 3)

print(f(3, 30, 0, 0))
