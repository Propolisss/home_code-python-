st = open('24_2427.txt').readline().strip()
maxx = float('-inf')
maxx_sub = ''
count = 0
temp = st[0]

for i in range(len(st) - 1):
    if st[i] > st[i + 1]:
        temp += st[i + 1]
        count += 1
        if count > maxx:
            maxx = count
            maxx_sub = temp
    else:
        temp = st[i + 1]
        count = 1
print(maxx_sub, maxx)