file = open('100.txt')
s = []

for i in file:
    s.extend(i.split())

count = 0

for i in range(len(s)):
    st = ''
    for j in range(len(s[i])):
        if s[i][j].isalpha():
            st += s[i][j]
    s[i] = st

for i in s:
    if i == 'счастие':
        count += 1
print(count)