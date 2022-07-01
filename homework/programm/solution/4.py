st = open('24_demo.txt').readline()
count = 0
i = 0
maxx = 0

while i <= len(st):
    if st[i - 3: i] == 'XYZ':
        count += 3
        i += 3
        if count > maxx:
            maxx = count
    else:
        if 'X' in st[i - 3: i]:
            count += 1
            if 'Y' in st[i - 3: i]:
                count += 1
                i += 1
        if count > maxx:
            maxx = count
        count = 0
        i += 1
print(maxx)