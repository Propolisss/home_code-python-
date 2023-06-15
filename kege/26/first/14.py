file = open('26_732.txt')
n, k = map(int, file.readline().split())
dic = dict()

for i in file:
    nums = [int(j) for j in i.split()]
    benef = nums[1] // nums[0]
    if benef in dic:
        dic[benef].append(nums)
    else:
        dic[benef] = [nums]

maxx = float('-inf')
maxx_cost = float('-inf')
summ = 0
for i in range(max(dic) + 1):
    if i in dic:
        dic[i].sort(reverse=True)
        for j in range(len(dic[i])):
            if k != 0:
                summ += dic[i][j][0]
                if dic[i][j][0] > maxx:
                    maxx = dic[i][j][0]
                    maxx_cost = dic[i][j][1]
                k -= 1
    if k == 0:
        break
print(summ, maxx_cost)