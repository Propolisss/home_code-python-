nums = [i.split() for i in open('4.txt')]
a = [0] * 1000
b = [0] * 1000
c = [0] * 1000

for s in nums:
    if s[-1] == 'A':
        for i in range(int(s[1]), int(s[2]) + 1):
            a[i] += 1
    if s[-1] == 'B':
        for i in range(int(s[1]), int(s[2]) + 1):
            b[i] += 1
    if s[-1] == 'C':
        for i in range(int(s[1]), int(s[2]) + 1):
            c[i] += 1
maxx = float('-inf')

for i in range(200):
    j = i
    count = 0
    while j < 200 and all(k >= 2 for k in [a[j], b[j], c[j]]):
        count += 1
        j += 1
    maxx = max(maxx, count)
print(maxx)