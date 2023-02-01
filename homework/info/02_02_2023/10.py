file = open('10.txt')

s = []
for i in file:
    s.extend(i.split())
count = 0

for i in range(len(s)):
    temp = ''
    for j in s[i]:
        if j.isalpha():
            temp += j
    s[i] = temp
for i in s:
    if i == 'теперь':
        count += 1
print(count)