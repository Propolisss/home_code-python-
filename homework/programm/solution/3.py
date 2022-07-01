st = input()
s = ''

for i in range(len(st)):
    if st[i] not in s:
        s += st[i]
s = s.replace(' ', '')
print(s)