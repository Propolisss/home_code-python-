st = open('24_2422.txt').readline()
maxx = float('-inf')
count = 1

for i in range(len(st) - 1):
    if st[i] <= st[i + 1]:
        count += 1
        maxx = max(maxx, count)
    else:
        count = 1
print(maxx)