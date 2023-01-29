st = 'ABCD BEF CBFGHDI DI ELG FEG GLMKJ HG IHGJ JK KM LM'
dic = {s[0] : s[1:] for s in st.split()}

def f(start, end):
    if start[-1] == end:
        return 'E' in start
    return sum(f(start + s, end) for s in dic[start[-1]] if s not in start)
print(f('A', 'M'))