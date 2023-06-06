s = 'АБЖ БЗВ ВГ ГЗЖД ДЖАЕК ЕИА ЖЗ ЗАВ ИА КЕ'
dic = {st[0] : st[1:] for st in s.split()}

def f(start, end):
    if start[-1] == end:
        return 1
    return sum(f(start + let, end) for let in dic[start[-1]] if let not in start)

print(f('В', 'З') + f('А', 'З'))