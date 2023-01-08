dic = {}
s = open('24 (3).txt').readline()

for i in range(2, len(s)):
    if s[i - 1] == s[i]:
        if s[i - 2] in dic:
            dic[s[i - 2]] += 1
        else:
            dic[s[i - 2]] = 1

maxx = float('-inf')
maxx_let = 'Z'

for i in dic:
    if dic[i] > maxx:
        maxx = dic[i]
        maxx_let = i
    elif dic[i] == maxx:
        if i < maxx_let:
            maxx_let = i
print(maxx_let, maxx, sep='')
