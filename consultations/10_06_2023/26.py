file = open('26_8482.txt')
n = int(file.readline())
k = int(file.readline())
nums = sorted([list(map(int, i.split())) for i in file])
dic = dict()
tables = dict()

for i in range(k):
    tables[i] = [0, 0]
maxx_time = float('-inf')

for i in nums:
    if i[0] in dic:
        dic[i[0]].append(i[1])
        dic[i[0]].sort()
    else:
        dic[i[0]] = [i[1]]
    maxx_time = max(maxx_time, i[0])

def find_table(num):
    minn_id = float('inf')
    minn = float('inf')
    for i in tables:
        if tables[i][1] <= num:
            return (i, 0)
    for i in tables:
        if (tables[i][1] - num) < minn:
            minn_id = i
            minn = tables[i][1] - num
    return (minn_id, minn)

count = 0
last = float('-inf')
for i in range(maxx_time + 1):
    if i in dic:
        for j in dic[i]:
            idd = find_table(i)
            if j + int(idd[1]) > (23 * 60):
                continue
            if 0 <= idd[1] <= 10:
                if idd[1] == 0:
                    tables[idd[0]] = [i, j + 6]
                else:
                    tables[idd[0]] = [i + idd[1], j + 6 + idd[1]]
                count += 1
                last = idd[0]
print(count, last + 1)