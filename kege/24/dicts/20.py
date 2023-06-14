st = ''
maxx = float('-inf')
maxx_let = ''
maxx_s = ''

for s in open('24_2507.txt'):
    st += s.strip()
    count = 1
    local_maxx = float('-inf')
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
            local_maxx = max(local_maxx, count)
        else:
            local_maxx = max(local_maxx, count)
            count = 1
    if local_maxx > maxx:
        maxx = local_maxx
        maxx_s = s
dic = {let : maxx_s.count(let) for let in sorted(set(maxx_s))}
maxx = max(dic.values())
print([i for i in dic if dic[i] == maxx], st.count('K'), maxx)