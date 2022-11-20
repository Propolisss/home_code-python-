from itertools import *
ans = set()

s = list(map(''.join, product('10789', repeat=4)))
print(len(s))
for i in s:
    st = i
    while '900' in st or '70' in st or '8' in st:
        st = st.replace('900', '8000', 1)
        st = st.replace('70', '900', 1)
        st = st.replace('8', '70', 1)
        if len(st) == 71 and st[0] == 'static':
            ans.add(int(i))
        elif len(st) > 71:
            break
print(sorted(ans))
