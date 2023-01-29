st = 'АБВ БГВ ВГ ГДЕЗЖ ДИЕ ЕИКЗ ЖЗЛ ЗКЛ ИКМ КМ ЛКМ'
dic = {s[0] : s[1:] for s in st.split()}

def f(start, end):
    if start[-1] == end:
        return 'Е' in start
    return sum(f(start + s, end) for s in dic[start[-1]] if s not in start)
print(f('А', 'М'))