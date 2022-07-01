st = open('zadanie24_1.txt').readline()
count = 0
i = 0
maxx = 0

while i <= len(st):
    if st[i - 2: i] == 'AB':
        count += 2
        i += 2
        if count > maxx:
            maxx = count
    else:
        if 'A' in st[i - 2: i]:
            count += 1
        if count > maxx:
            maxx = count
        count = 0
        i += 1
print(maxx)