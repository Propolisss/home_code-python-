file = open('26_1868.txt')
n = int(file.readline())
dic = dict()
maxx = float('-inf')
minn_id = float('inf')

for i in file:
    nums = [int(j) for j in i.split()]
    if nums[0] in dic:
        dic[nums[0]].add(nums[1])
    else:
        dic[nums[0]] = {nums[1]}

ans = dict()
for i in range(max(dic) + 1):
    if i in dic:
        dic[i] = sorted(dic[i])
        for j in range(len(dic[i]) - 1):
            if dic[i][j + 1] - dic[i][j] == 3:
                maxx = i
                if i in ans:
                    ans[i].append(dic[i][j] + 1)
                else:
                    ans[i] = [dic[i][j] + 1]
print(maxx, ans[maxx])