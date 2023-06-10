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
    # if any(tables[i][1] == 0 for i in tables):
    #     for i in tables:
    #         if tables[i][1] == 0:
    #             return (i, 0)
    # elif any(tables[i][1] < num for i in tables):
    #     for i in tables:
    #         if tables[i][1] < num:
    #             return (i, 0)
    for i in tables:
        if tables[i][1] < num:
            return (i, 0)
        # elif tables[i][1] == num:
        #     return (i, 'True')
    if any(tables[i][1] == num for i in tables):
        for i in tables:
            if tables[i][1] == num:
                return (i, 'True')
    for i in tables:
        if (tables[i][1] - num) < minn:
            minn_id = i
            minn = tables[i][1] - num
    if minn < 0:
        return (minn_id, 0)
    elif minn > 0:
        return (minn_id, minn)
    return (minn_id, 0)

count = 0
last = float('-inf')
ll = 0
for i in range(maxx_time + 1):
    if i in dic:
        for j in dic[i]:
            idd = find_table(i)
            ll = tables[idd[0]]
            if idd[1] == 'True':
                if j + 1 > (23 * 60):
                    continue
            elif idd[1] != 0:
                if j + int(idd[1]) + 1 > (23 * 60):
                    continue
            else:
                if j > (23 * 60):
                    continue
            if idd[1] == 'True' or 0 <= idd[1] <= 10:
                if idd[1] == 0:
                    tables[idd[0]] = [i, j + 5]
                elif idd[1] == 'True':
                    tables[idd[0]] = [i + 1, j + 5 + 1]
                # elif idd[1] == 0:
                #     tables[idd[0]] = [i, j + 5]
                else:
                    tables[idd[0]] = [i + idd[1] + 1, j + 5 + idd[1] + 1]

                #tables[idd[0]] = [i if count < k else i + idd[1] + 1, j + 5 if count < k else j + 5 + idd[1] + 1]
                count += 1
                last = idd[0]
                print(tables[last], i, j, idd[0] + 1, idd[1], ll)
print(count, last + 1)