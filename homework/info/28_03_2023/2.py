file = open('24_1064.txt')
s = [i.strip() for i in file]
ans = [set() for _ in range(len(s))]
all_ans = []
for i in range(len(s)):
    j = 0
    temp_st = s[i][j]

    while j < len(s[i]):
        if s[i][j] == s[i][j - 1]:
            temp_st += s[i][j - 1]
            j += 1
            ans[i].add(temp_st)
            all_ans.append(temp_st)
        else:
            temp_st = s[i][j]
            j += 1
dic = dict()

for i in ans:
    maxx = float('-inf')
    for j in i:
        maxx = max(maxx, len(j))

    for j in all_ans:
        if len(j) == maxx:
            if j[0] in dic:
                dic[j[0]] += 1
            else:
                dic[j[0]] = 1
print(dic)