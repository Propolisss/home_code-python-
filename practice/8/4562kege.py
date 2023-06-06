from functools import *
@lru_cache(None)
def f(lenn, prev, curr):
    if lenn == 16:
        return curr != 'S'
    summ = 0

    for i in 'CONST':
        if lenn == 1:
            summ += f(lenn + 1, curr, i) if curr != i else 0
        else:
            if curr == 'S':
                summ += f(lenn + 1, curr, i) if i != prev and i != 'S' else 0
            else:
                summ += f(lenn + 1, curr, i) if i != curr else 0
    return summ
print(sum(f(1, '', let) for let in 'CONT'))