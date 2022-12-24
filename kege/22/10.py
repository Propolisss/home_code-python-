nums = [i.replace(';', ' ').split() for i in open('22.txt')]

for i in range(len(nums)):
    for j in range(len(nums[i])):
        if nums[i][j] == '?':
            ind = [i, j]
            break
id = []
for i in nums:
    id.append(i[0])

for x in id:
    nums[ind[0]][ind[1]] = x
    dic = {'0' : 0}
    count = 0
    while len(dic) < len(nums) + 1:
        count += 1
        for s in nums:
            if all(sub in dic for sub in s[2:]):
                dic[s[0]] = int(s[1]) + max(dic[sub] for sub in s[2:])
        if count > 100:
            break
    if max(dic.values()) == 154:
        print(x)
        break