file = open('26_788.txt')
d, e, n = map(int, file.readline().split())
nums = sorted([int(i) for i in file])
dd = sorted([i for i in nums if i > 500])
ee = sorted([i for i in nums if i <= 500])
summ_d = 0
maxx_d = float('-inf')
summ_e = 0
maxx_e = float('-inf')
count = 0
last = 0

for i in range(len(dd)):
    if summ_d + dd[i] <= d:
        summ_d += dd[i]
        maxx_d = max(maxx_d, dd[i])
        count += 1
        last = dd[i]
for i in range(len(dd) - 1, -1, -1):
    if summ_d - last + dd[i] <= d:
        summ_d += dd[i] - last
        maxx_d = max(maxx_d, dd[i])
        break

for i in range(len(ee)):
    if summ_e + ee[i] <= e:
        summ_e += ee[i]
        maxx_e = max(maxx_e, ee[i])
        count += 1
        last = ee[i]
for i in range(len(ee) - 1, -1, -1):
    if summ_e - last + ee[i] <= e:
        summ_e += ee[i] - last
        maxx_e = max(maxx_e, ee[i])
        break
print(count, maxx_d + maxx_e)