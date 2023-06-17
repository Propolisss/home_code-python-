st = 'АБВГД БВЕ ВГЖ ГДЖ ДЖЗ ЕВЖИ ЖИ ЗЖИ ИКЛ КМ ЛКМ'
dic = {s[0] : s[1:] for s in st.split()}

def f(start, end):
    if start[-1] == end:
        return len(start) <= 8 and 'Ж' in start and 'Г' not in start
    return sum(f(start + let, end) for let in dic[start[-1]] if let not in start)
print(f('А', 'М'))