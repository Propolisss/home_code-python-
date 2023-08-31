pmi = open('pmi_mai.txt')
fiit = open('fiit_mai.txt')
subs = dict()

for i in pmi:
    s = i.replace(',', ' ').split()
    while any(j in s[0] for j in '0123456789'):
        del s[0]
    count = 0
    for j in range(len(s)):
        if s[j].isdigit():
            count += 1
            if count == 1:
                start = j
            if int(s[j]) > 25:
                ind = j
                break
    if ' '.join(s[:start]) in subs:
        subs[' '.join(s[:start])][0] = s[ind]
    else:
        subs[' '.join(s[:start])] = [s[ind], 0]

for i in fiit:
    s = i.replace(',', ' ').split()
    while any(j in s[0] for j in '0123456789'):
        del s[0]
    count = 0
    for j in range(len(s)):
        if s[j].isdigit():
            count += 1
            if count == 1:
                start = j
            if int(s[j]) > 25:
                ind = j
                break
    if ' '.join(s[:start]) in subs:
        subs[' '.join(s[:start])][1] = s[ind]
    else:
        subs[' '.join(s[:start])] = [0, s[ind]]

summ_pmi = 0
summ_fiit = 0
for i in subs:
    summ_pmi += int(subs[i][0])
    summ_fiit += int(subs[i][1])
    if subs[i][0] != subs[i][1]:
        print(f'{i} пми: {subs[i][0]} фиит: {subs[i][1]}')
print(summ_pmi, summ_fiit)