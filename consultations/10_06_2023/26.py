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
        dic[i[0]] = min(dic[i[0]], i[1])
    else:
        dic[i[0]] = i[1]
    maxx_time = max(maxx_time, i[0])

def find_table(num):
    minn_id = float('inf')
    minn = float('inf')
    if any(tables[i][1] <= num for i in tables):
        for i in tables:
            if tables[i][1] <= num:
                return (i, 0)
    else:
        for i in tables:
            if (tables[i][1] - num) < minn:
                minn_id = i
                minn = tables[i][1] - num
    if minn != 0:
        return (minn_id, minn)
    return (minn_id, 0)
count = 0
last = float('-inf')
for i in range(maxx_time + 1):
    if i in dic:
        if dic[i] >= (23 * 60):
            continue
        idd = find_table(i)
        if 0 <= abs(idd[1]) <= 10:
            tables[idd[0]] = [i if count < k else i + 1 + idd[1], dic[i] + 5 if count < k else dic[i] + 6 + abs(idd[1])]
            count += 1
            last = idd[0]
print(count, last + 1)