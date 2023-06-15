file = open('26_2613.txt')
n = int(file.readline())
dic = dict()
maxx = float('-inf')
maxx_id = ''

for i in file:
    nums = [int(j) for j in i.split()]
    if nums[0] in dic:
        dic[nums[0]].add(nums[1])
    else:
        dic[nums[0]] = {nums[1]}

for i in range(max(dic) + 1):
    if i in dic:
        local_max = float('-inf')
        dic[i] = sorted(dic[i])
        count = 1
        for j in range(len(dic[i]) - 1):
            if dic[i][j + 1] - dic[i][j] == 1:
                count += 1
                local_max = max(local_max, count)
            else:
                count = 1
        if local_max >= maxx:
            maxx = local_max
            maxx_id = i
print(maxx_id, maxx)