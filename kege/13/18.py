st = 'АБГД БВГ ВЗКЕ ГВЕЖ ДГ ЕИМКЖ ЖИ ЗКЛ ИМ КЛНМ ЛН МН'
dic = {s[0] : s[1:] for s in st.split()}

def f(start, end):
    if start[-1] == end:
        return ('Г' in start) + ('Е' in start) == 1
    return sum(f(start + s, end) for s in dic[start[-1]] if s not in start)
print(f('А', 'Н'))