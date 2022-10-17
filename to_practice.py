from functools import lru_cache

# pust = ''
#
# @lru_cache
# def f(start, end, current, pust):
#     previous = pust[:]
#     previous += str(current)
#     for i in range(1, len(previous)):
#         if previous[i - 1] == 3 and previous[i] == 3:
#             return 0
#     if start > end or start == 28:
#         return 0
#     if start == end:
#         #print(previous)
#         previous = previous[:-1]
#         return 1
#     else:
#         f1 = f(start + 1, end, 1, previous)
#         f2 = f(start + 3, end, 2, previous)
#         f3 = f(start * 2, end, 3, previous)
#         return f1 + f2 + f3
# print(f(4, 10, 0, pust) * f(10, 93, 0, pust))


def add1(num): return num + 1
def add2(num): return num + 2
def pr(num): return num * 2




@lru_cache()
def f(start, end, count, repeat=False):
    if start > end:
        return 0
    if start == 23:
        return 0
    if start == 11:
        count += 1
    if start == end and count == 1:
        return 1

    if repeat:
        return f(add2(start), end, count) + f(pr(start), end, count)
    else:
        return f(add1(start), end, count, True) + f(add2(start), end, count) + f(pr(start), end, count)

print(f(3, 79, 0))
