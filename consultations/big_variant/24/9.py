st = open('24_7891.txt').readline()
maxx = float('-inf')

for i in set(st):
    temp = st
    temp = temp.split(i)
    maxx = max(maxx, max(len(j) for j in temp) + 2)
print(maxx)