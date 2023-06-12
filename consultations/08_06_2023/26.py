file = open('26-95.txt')
n = int(file.readline())
dic = dict()
maxx_id = float('-inf')

for i in file:
    nums = [int(j) for j in i.split()]
    if nums[0] in dic:
        dic[nums[0]][nums[1]] = 1
    else:
        dic[nums[0]] = [0] * 5001
        dic[nums[0]][nums[1]] = 1
    maxx_id = max(maxx_id, nums[0])

count = 0
maxx_home = float('-inf')
ans = dict()

for i in range(maxx_id + 1):
    if i in dic:
        for j in range(len(dic[i])):
            if j >= 3 and j <= (len(dic[i]) - 3):
                if dic[i][j] == 0 and (sum(dic[i][j + 1: j + 4]) + sum(dic[i][j - 3:j])) >= 3:
                    if i in ans:
                        ans[i].append(j)
                    else:
                        ans[i] = [j]
                    maxx_home = max(maxx_home, i)
            elif j <= 3:
                if dic[i][j] == 0 and sum(dic[i][j + 1: j + 4]) + sum(dic[i][:j]) >= 3:
                    if i in ans:
                        ans[i].append(j)
                    else:
                        ans[i] = [j]
                    maxx_home = max(maxx_home, i)
            elif j >= len(dic[i]) - 3:
                if dic[i][j] == 0 and sum(dic[i][j - 3 : j]) + sum(dic[i][j + 1:]) >= 3:
                    if i in ans:
                        ans[i].append(j)
                    else:
                        ans[i] = [j]
                    maxx_home = max(maxx_home, i)

print(len(ans), min(ans[maxx_home]))