st = open('24-191.txt').readline()

temp_st = ''
count = 0
for i in range(len(st) - 15):
    for j in range(15):
        temp_st += st[i + j]
        if (temp_st[0] == 'A') and ('F' in temp_st) and (temp_st[-1] == 'B') and ('A' not in temp_st[1:-1]) and ('B' not in temp_st[1:-1]):
            count += 1
    temp_st = ''
print(count)