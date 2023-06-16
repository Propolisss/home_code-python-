file = open('26_2650.txt')
l, m, n = map(int, file.readline().split())
day = [0] * (l + 1)

for i in file:
    st, end = [int(j) for j in i.split()]
    day[st] += 1
    day[st + end] -= 1

k = 0
st = -1
end = 0
prev = 0
maxx = float('-inf')
count = 0

for i in range(l + 1):
    prev = k
    k += day[i]
    if k == 0 and st == -1:
        st = i
    if prev == 0 and (k > 0 or i == l):
        end = i
        maxx = max(maxx, end - st)
        if (end - st) >= m:
            count += 1
        st, end = -1, 0
print(count, maxx)