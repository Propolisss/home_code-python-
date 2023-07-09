uy7_old = open('uy7_old.txt')
uy7_new = open('uy7_new.txt')
uy9 = open('uy9.txt')
all_plans = dict()

for i in uy7_old:
    s = i.strip().split()
    count = 0
    if s[0].isdigit():
        s.pop(0)
    for j in range(len(s)):
        if s[j].isdigit():
            count += 1
            if int(s[j]) > 30:
                ind = j
                break
    st = ' '.join(s[:ind - 2]) if count == 2 else ' '.join(s[:ind - 1])
    if st in all_plans:
        all_plans[st][0] = s[ind]
    else:
        all_plans[st] = [0, 0, 0]
        all_plans[st][0] = s[ind]

for i in uy7_new:
    s = i.strip().split()
    count = 0
    if s[0].isdigit():
        s.pop(0)
    for j in range(len(s)):
        if s[j].isdigit():
            count += 1
            if int(s[j]) > 30:
                ind = j
                break
    st = ' '.join(s[:ind - 2]) if count == 2 else ' '.join(s[:ind - 1])
    if st in all_plans:
        all_plans[st][1] = s[ind]
    else:
        all_plans[st] = [0, 0, 0]
        all_plans[st][1] = s[ind]

for i in uy9:
    s = i.strip().split()
    count = 0
    if s[0].isdigit():
        s.pop(0)
    for j in range(len(s)):
        if s[j].isdigit():
            count += 1
            if int(s[j]) > 30:
                ind = j
                break
    st = ' '.join(s[:ind - 2]) if count == 2 else ' '.join(s[:ind - 1])
    if st in all_plans:
        all_plans[st][2] = s[ind]
    else:
        all_plans[st] = [0, 0, 0]
        all_plans[st][2] = s[ind]

for i in sorted(all_plans):
    if all_plans[i][2] != 0:
        print(i, all_plans[i][2])