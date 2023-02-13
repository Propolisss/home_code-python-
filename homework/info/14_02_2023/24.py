st = open('24 (3).txt').readline()

maxx = float('-inf')
i = 0
count = 0

# while i < len(st):
#     if st[i : i + 2] not in ['ad', 'da'] and st[i - 1 : i + 1] not in ['ad', 'da']:
#         count += 2
#         i += 2
#         maxx = max(maxx, count)
#     else:
#         i += 1
#         maxx = max(maxx, count)
#         count = 0
# print(maxx)

for i in range(len(st)):
    temp_st = ''
    print(i)
    for j in range(i, len(st)):
        temp_st += st[j]
        if 'ad' not in temp_st and 'da' not in temp_st:
            maxx = max(maxx, len(temp_st))
        else:
            break
print(maxx)