nums = [i.replace(';', ' ').split() for i in open('22.txt')]

for i in range(len(nums)):
    for j in range(len(nums[i])):
        if nums[i][j] == 't':
            ind = [i, j]
            break

maxx = float('-inf')
for x in range(200):
    dic = {'0' : 0}
    nums[ind[0]][ind[1]] = str(x)

    while len(dic) < len(nums) + 1:
        for s in nums:
            if all(sub in dic for sub in s[2:]):
                dic[s[0]] = int(s[1]) + max(dic[sub] for sub in s[2:])
    if max(dic.values()) <= 107:
        maxx = max(maxx, x)
print(maxx)