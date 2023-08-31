st = '1254 213456 3256 412578 512346789 623589 7458 874569 9568'
st = {s[0] : s[1:] for s in st.split()}
ans = set()

def f(start):
    if len(start) >= 10:
        return
    elif len(start) >= 4:
        ans.add(start)
    for i in st[start[-1]]:
        if i not in start:
            f(start + i)

for i in '123456789':
    f(i)
print(sorted(ans, reverse=1))