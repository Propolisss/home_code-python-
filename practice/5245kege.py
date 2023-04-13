file = open('26.txt')
n = int(file.readline())
dic = {int(sub.replace(';', ' ').split()[0]) : list(map(int, sub.replace(';', ' ').split()))[1:] for sub in file}
starter_cost = {i : int(dic[i][0]) for i in dic}
minn = float('inf')
maxx = float('-inf')

for i in dic:
    for j in range(1, len(dic[i])):
        r = len(dic[i]) - 1
        ind = dic[i][j]
        dic[ind][0] += dic[i][0] * (r / 100)
        dic[i][0] -= dic[i][0] * (r / 100)

ans = []
for i in dic:
    cost = dic[i][0] / starter_cost[i] * 100
    if cost < minn:
        minn = cost
        minn_id = i
    if cost > maxx:
        maxx = cost
        maxx_id = i
    ans.append([cost, i, dic[i][0], starter_cost[i]])
ans.sort()
print(minn_id, maxx_id)