s = 'АБ БВ ВЖЕГ ГЕД ДЕЖК ЕЖ ЖНЗ ЗЛКД КЛ ЛМ МАНЗ НАБВ'
dic = {st[0] : st[1:] for st in s.split()}

def f(start, end):
    if start[-1] == end and len(start) > 1:
        return 1
    return sum(f(start + let, end) for let in dic[start[-1]] if let not in start[1:])
print(f('Ж', 'Ж'))