st = open('24-4.txt').readline()
maxx = float('-inf')

for i in range(len(st)):
    temp_st = st[i]
    for j in range(i + 1, len(st)):
        if st[j] == '\n':
            continue
        temp_st += st[j]
        if all(ord(temp_st[k - 1]) > ord(temp_st[k]) for k in range(1, len(temp_st))):
            maxx = max(maxx, len(temp_st))
        else:
            break
print(maxx)
