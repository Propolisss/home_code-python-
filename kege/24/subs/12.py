st = open('24_2423.txt').readline().strip()
maxx = float('-inf')
count = 1

for i in range(len(st) - 1):
    if int(st[i]) < int(st[i + 1]):
        count += 1
        maxx = max(maxx, count)
    else:
        count = 1
print(maxx)