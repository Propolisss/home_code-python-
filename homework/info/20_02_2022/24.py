st = open('24 (3).txt').readline()
nums = '0123456789'

temp_st = ''
count = 0
for i in range(1, len(st)):
    if st[i - 1] not in nums:
        temp_st += st[i - 1]
    else:
        if len(temp_st) == 5:
            count += 1
        temp_st = ''
print(count)