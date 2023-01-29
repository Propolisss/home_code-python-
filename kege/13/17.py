st = 'АБВГД БЕВ ВЖ ГВЖ ДГЖЗ ЕЖИ ЖИ ЗЖИ ИКЛМ КМ ЛМ'
dic = {s[0] : s[1:] for s in st.split()}

def f(start, end):
    if start[-1] == end:
        return ('К' not in start and 'Ж' in start)
    return sum(f(start + s, end) for s in dic[start[-1]] if s not in start)
print(f('А', 'М'))