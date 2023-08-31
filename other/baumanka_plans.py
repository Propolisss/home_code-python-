uy7_old = open('uy7_old.txt')
uy7_new = open('uy7_new.txt')
uy9 = open('uy9.txt')
uy5 = open('uy5.txt')
uy6 = open('uy6.txt')
new_uy6 = open('new_omg_uy6.txt')
all_plans = dict()
uy5_uy6_plans = dict()

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

for i in uy5:
    s = i.strip().split()
    if s[0].isdigit():
        s.pop(0)
    first_num = 0
    for j in range(len(s)):
        if s[j].isdigit():
            if first_num == 0:
                first_num = j
            if int(s[j]) > 40:
                ind = j
                break
    if ' '.join(s[:first_num - 1]) in uy5_uy6_plans:
        uy5_uy6_plans[' '.join(s[:first_num - 1])][0] = s[ind]
    else:
        uy5_uy6_plans[' '.join(s[:first_num - 1])] = [s[ind], 0, 0]
for i in uy6:
    s = i.strip().split()
    if s[0].isdigit():
        s.pop(0)
    first_num = 0
    for j in range(len(s)):
        if s[j].isdigit():
            if first_num == 0:
                first_num = j
            if int(s[j]) > 40:
                ind = j
                break
    if ' '.join(s[:first_num - 1]) in uy5_uy6_plans:
        uy5_uy6_plans[' '.join(s[:first_num - 1])][1] = s[ind]
    else:
        uy5_uy6_plans[' '.join(s[:first_num - 1])] = [0, s[ind], 0]
for i in new_uy6:
    s = i.strip().split()
    if s[0].isdigit():
        s.pop(0)
    first_num = 0
    for j in range(len(s)):
        if s[j].isdigit():
            if first_num == 0:
                first_num = j
            if int(s[j]) > 40:
                ind = j
                break
    if ' '.join(s[:first_num - 1]) in uy5_uy6_plans:
        uy5_uy6_plans[' '.join(s[:first_num - 1])][2] = s[ind]
    else:
        uy5_uy6_plans[' '.join(s[:first_num - 1])] = [0, 0, s[ind]]
math_hours = []
count_math_hours = 0

for i in uy5_uy6_plans:
    if uy5_uy6_plans[i][1] == uy5_uy6_plans[i][2] and (int(uy5_uy6_plans[i][1]) + int(uy5_uy6_plans[i][2])) > 0:
        print(i, uy5_uy6_plans[i][1], uy5_uy6_plans[i][2])
    # if uy5_uy6_plans[i][1] != 0:
    #     print(i, uy5_uy6_plans[i][1])
    #     s = input()
    #     if s == 'да':
    #         count_math_hours += int(uy5_uy6_plans[i][1])
    #         math_hours.append([i, uy5_uy6_plans[i][1]])

# for i in math_hours:
#     print(*i)
# else:
#     print(f'общее кол-во {count_math_hours}')