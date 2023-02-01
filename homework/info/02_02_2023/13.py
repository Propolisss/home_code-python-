st = 'АБГ БД ВГАБД ГЕЖ ДИЛЕ ЕЛВ ЖЕ ИЛ КЖ ЛЖК'
dic = {s[0] : s[1:] for s in st.split()}

def f(start, end):
    if start[-1] == end and len(start) > 1:
        return 1
    return sum(f(start + s, end) for s in dic[start[-1]])
print(f('Е', 'Е'))