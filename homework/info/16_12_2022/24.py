st = open('24 (3).txt').readline()


maxx_len = float('-inf')
curr_len = 5

for i in range(len(st) - 5):
    if st[i:i + 3] != st[i + 3:i + 6]:
        curr_len += 1
    else:
        maxx_len = max(maxx_len, curr_len)
        curr_len = 5
print(maxx_len)