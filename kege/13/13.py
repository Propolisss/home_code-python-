st = 'АБГДЕ БВ ВИЖ ГВЖБД ДЖЗ ЕДЗК ЖЛ ЗЖЛ ИЖЛ КЗЛМ МЛ'
dic = {s[0] : s[1:] for s in st.split()}

def f(start, end):
    if start[-1] == end:
        return 'З' not in start and 'Ж' in start
    return sum(f(start + s, end) for s in dic[start[-1]] if s not in start)
print(f('А', 'Л'))