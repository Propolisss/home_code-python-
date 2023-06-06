from functools import *

@lru_cache(None)
def f(gl, sogl):
    if gl + sogl == 10:
        return gl == sogl
    summ = 0

    for i in 'ЕВЛАМПИЙ':
        summ += f(gl + 1 if i in 'ЕАИ' else gl, sogl + 1 if i in 'ВЛМПЙ' else sogl)
    return summ
print(sum(f(1 if let in 'ЕАИ' else 0, 1 if let in 'ВЛМПЙ' else 0) for let in 'ЕВЛАМПИЙ'))