st = open('24_2425.txt').readline().strip()
maxx = float('-inf')
count = 0
i = 0

while i < len(st) - 3:
    if st[i : i + 4] == 'DBAC':
        count += 4
        i += 4
        maxx = max(maxx, count)
    elif st[i - 4 : i] == 'DBAC':
        temp_st = ''
        for temp in range(i, i + 4):
            if 'DBAC'.startswith(temp_st + st[temp]):
                temp_st += st[temp]
            else:
                break
        maxx = max(maxx, count + len(temp_st))
        count = 0
        i += 1
    else:
        count = 0
        i += 1
print(maxx)