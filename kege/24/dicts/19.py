maxx = float('-inf')
maxx_s = ''
st = ''

for s in open('24_2508.txt'):
    if s.count('Q') >= maxx:
        maxx = s.count('Q')
        maxx_s = s.strip()
    st += s

dic = {let : maxx_s.count(let) for let in sorted(set(maxx_s))}
minn = min(dic.values())
print([i for i in dic if dic[i] == minn], st.count('C'))