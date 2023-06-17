st = open('24_5677.txt').readline()
temp = ''
for i in range(1, 1000):
    if 'DAD' * i not in st:
        temp = 'DAD' * (i - 1)
        break
maxx = float('-inf')
for i in ['AD', 'D', '']:
    for j in ['DA', 'D', '']:
        if (i + temp + j) in st:
            maxx = max(maxx, len(i + temp + j))
print(maxx)