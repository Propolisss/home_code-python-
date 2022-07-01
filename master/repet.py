st = input()
count = 1
maxx = 0

if len(st) == 1:
    maxx = 1

for i in range(1, len(st)):
    if st[i - 1] == st[i]:
        count += 1
        maxx = max(maxx, count)
    else:
        maxx = max(maxx, count)
        count = 1
print(maxx)