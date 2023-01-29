st = 'АВ БАГЖ ВБД ГЖ ДЗ ЖЗД ЗВБ'
dic = {s[0] : s[1:] for s in st.split()}
ans = set()
def f(start, end):
    if start[-1] == end and len(start) > 1:
        ans.add(start)
        return 1
    return sum(f(start + s, end) for s in dic[start[-1]] if start.count(s) <= 1)
print(f('Г', 'Г'))
print(len(ans))