st = open('24 (3).txt').readline().replace('B', 'A').replace('2', '1')
maxx = float('-inf')

for i in range(len(st)):
    j = i
    temp_st = ''
    count = 0

    while j < len(st):
        temp_st += st[j]
        if len(temp_st) % 3 == 0:
            if temp_st[-3:] == '11A':
                count += 1
            else:
                maxx = max(maxx, count)
                break
        j += 1
    maxx = max(maxx, count)
print(maxx)