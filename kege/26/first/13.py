file = open('26_2616.txt')
n, s = map(int, file.readline().split())
dic = dict()

for i in file:
    nums = [int(j) for j in i.split()]
    if nums[0] in dic:
        dic[nums[0]].append(nums[1])
    else:
        dic[nums[0]] = [nums[1]]

count = 0
maxx_diff = float('-inf')
maxx_id = ''
for i in range(max(dic) + 1):
    if i in dic:
        dic[i].sort()
        summ = 0
        local_count = 0
        for j in range(len(dic[i])):
            if summ + dic[i][j] <= s:
                summ += dic[i][j]
                local_count += 1
                count += 1
            else:
                break
        dif = len(dic[i]) - local_count
        if dif > maxx_diff:
            maxx_diff = dif
            maxx_id = i
print(n - count, maxx_id)