st = 'АБВГД БЕВ ВЖ ГВЖ ДГЖЗ ЕЖИ ЖИ ЗЖИ ИКЛ КМ ЛМК'
dic = {s[0] : s[1:] for s in st.split()}

def f(start, end):
    if start[-1] == end:
        return len(start) - 1
    return max(f(start + s, end) for s in dic[start[-1]] if s not in start)
print(f('А', 'М'))