st = 'АВ БАД ВБЕ ГВБД ДЗ ЕЖ ЖГК ЗГЖ КЗ'
dic = {s[0] : s[1:] for s in st.split()}

def f(start, end):
    if start[-1] == end and len(start) > 1:
        return 1
    return sum(f(start + let, end) for let in dic[start[-1]] if let not in start[1:])
print(f('Ж', 'Ж'))