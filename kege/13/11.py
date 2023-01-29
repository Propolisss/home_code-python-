st = 'АБВГ БДВ ВДЖ ГВЕ ДИЖ ЕЖК ЖК ИК'
dic = {s[0] : s[1:] for s in st.split()}

def f(start, end):
    if start[-1] == end:
        return 1
    return sum(f(start + s, end) for s in dic[start[-1]] if s not in start)
print(f('А', 'К'))