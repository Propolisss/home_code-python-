s = open('24 (3).txt').readline()


maxx = float('-inf')
for i in range(len(s)):
    temp_st = ''
    j = i

    while 'PP' not in temp_st and j < len(s):
        temp_st += s[j]
        j += 1
    maxx = max(maxx, len(temp_st) - 1)
print(maxx)