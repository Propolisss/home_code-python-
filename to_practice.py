from functools import lru_cache

delt = []
nums = []

#@lru_cache
def f(start, end, current):
    global nums
    global delt
    if len(delt) > 0:
        nums = delt[-1][:]
    nums.append(current)
    delt.append(nums[:])
    for i in range(1, len(delt[-1])):
        if delt[-1][i - 1] == 1 and delt[-1][i] == 1:
            del delt[-1]
            #delt.clear()
            nums.clear()
            return 0
    if start > end or start == 33:
        #delt.clear()
        nums.clear()
        return 0
    if start == end:
        #delt.clear()
        nums.clear()
        return 1
    else:
        return f(start * 2, end, 1) + f(start + 1, end, 2) + f(start + 3, end, 3)

print(f(2, 18, 0) * f(18, 51, 0))
