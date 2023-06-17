st = 'АБДЕ БВ ВЗЖГ ГАБ ДИ ЕДЗ ЖЗЛ ЗЛГ ИЕЗК КЗ ЛК'
dic = {s[0] : s[1:] for s in st.split()}

def f(start, end):
    if len(start) > 1 and start[-1] == end:
        return 1
    return sum(f(start + let, end) for let in dic[start[-1]] if let not in start[1:])
print(f('Г', 'Г'))