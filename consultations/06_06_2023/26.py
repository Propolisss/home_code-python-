file = open('26-96.txt')
n = int(file.readline())
dic = dict()
ans = dict()

for i in file:
    n1, n2 = map(int, i.split())
    if n2 in dic:
        dic[n2] += 1
        ans[n2].add(str(n1)[:-1])
    else:
        dic[n2] = 1
        ans[n2] = set([str(n1)[:-1]])
maxx = max(dic.values())

for i in dic:
    if dic[i] == maxx:
        print(i, len(ans[i]))