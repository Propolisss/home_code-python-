st = open('24.txt').readline()
glasn = 'AO'
sogl = 'FCD'

s = []

i = 1
j = 1
count = 0
maxx = 0

while i < len(st):
    print(i)
    if st[i - 1] in sogl and st[i] in glasn:
        while st[j - 1] in sogl and st[j] in glasn:
            count += 2
            j += 2
    else:
        maxx = max(maxx, count)
        count = 0
    i += 1
    j = i
print(maxx / 2)