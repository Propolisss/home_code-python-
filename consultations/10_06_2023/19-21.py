from math import floor
def f(start, count, target, maxx):
    if (floor(start * 1.25) > maxx) and (floor(start * 1.5) > maxx) and (floor(start * 1.75) > maxx) and (floor(start * 2.1) > maxx):
        return (count) % 2 == target % 2
    if count == target:
        return 0
    h = [f(floor(start * 1.25), count + 1, target, maxx), f(floor(start * 1.5), count + 1, target, maxx),
         f(floor(start * 1.75), count + 1, target, maxx), f(floor(start * 2.1), count + 1, target, maxx)]
    return any(h) if (count - 1) % 2 == target % 2 else all(h)
count = 0

for i in range(4, 172 + 1):
    if f(i, 0, 4, i + 215) and not(f(i, 0, 2, i + 215)):
        count += 1
        print(i)
print(count)