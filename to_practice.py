sn = open('24-208.txt').readline()
s = sn.replace('2022', '*')

count1 = 0
count6 = 0
counter = 0
maxx = 0
i = 0
temp_st = ''

while i < len(s):
    if s[i] == '*':
        counter += 1
        temp_st += '2022'
        if counter == 1:
            count1 = i
        if counter == 6:
            count6 = i
        if counter == 6:
            maxx = max(maxx, len(s[count1 + 1:count6].replace('*', '2022')) + 3)
            temp_st = ''
            counter = 0
            i = count1
            count1 = 0
            count6 = 0
    else:
        temp_st += s[i]
    i += 1
print(maxx)