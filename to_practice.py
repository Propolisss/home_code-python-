from functools import *
@lru_cache(None)
def f(lenn, count, prev, curr):
    if lenn == 10:
        return count == 5
    summ = 0

    for i in '01234567':
        if curr == '7':
            summ += f(lenn + 1, count + 1 if i == '7' else count, curr, i) if i not in '1357' else 0
        elif curr in '1357':
            summ += f(lenn + 1, count + 1 if i == '7' else count, curr, i) if i != '7' else 0
        else:
            summ += f(lenn + 1, count + 1 if i == '7' else count, curr, i)
    return summ
print(sum(f(1, 1 if let == '7' else 0, '', let) for let in '1234567'))