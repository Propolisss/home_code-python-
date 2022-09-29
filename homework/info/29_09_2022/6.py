delt = []

def f(start, end, count2, count):
    if start > end:
        return 0
    if len(delt) > 2:
        if count - count2 == delt[-3]:
            delt.clear()
            return 0
    if start == end:
        return 1
    else:
        delt.append(count - count2)
        return f(start + 1, end, count2, count + 1) + f(start + 3, end, count2 + 1, count + 1) + f(start * 2, end, count2, count + 1)

print(f(2, 20, 0, 0))
print(delt)