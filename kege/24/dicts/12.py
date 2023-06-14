count = 0

for s in open('24_2503.txt'):
    count_1 = 0
    count_2 = 0
    for i in range(len(s) - 2):
        if s[i : i + 3] == 'AOA':
            count_1 += 1
        if s[i : i + 3] == 'OAO':
            count_2 += 1
    if count_1 > count_2:
        count += 1
print(count)