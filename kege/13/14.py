st = 'ABCDE BFG CBGH DCH EDHI FJ GFJK HGK IHKL JM KJML LM'
dic = {s[0] : s[1:] for s in st.split()}

def f(start, end):
    if start[-1] == end:
        return 1
    return sum(f(start + s, end) for s in dic[start[-1]] if s not in start)
print(f('A', 'M'))