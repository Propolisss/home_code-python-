st = open('24-197.txt').readline().replace('ZXY', '*').replace('ZYX', '*')

count = 0
maxx = 0
temp_st = ''

for i in range(len(st)):
    if st[i] == '*':
        count += 1
    else:
        maxx = max(maxx, count)
        count = 0
print(maxx)