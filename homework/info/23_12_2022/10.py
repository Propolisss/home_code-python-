file = open('10 (4).txt')

s = []
for i in file:
    s.extend(i.split())

count = 0
for i in s:
    if i.lower() == 'день':
        count += 1
print(count)