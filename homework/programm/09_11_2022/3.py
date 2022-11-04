st = open('24-181 (2).txt').readline()
maxx = float('-inf')

for i in range(len(st)):
    j = i
    temp_st = ''

    while j < len(st) and st[j] not in 'AEIOUY':
        temp_st += st[j]
        j += 1

    if temp_st.count('.') >= 6:
        maxx = max(maxx, len(temp_st))
print(maxx)