file = open('27B.txt')
n = int(file.readline())
nums = [int(i) for i in file]
dic = dict()

for i in nums:
    summ = sum(int(j) for j in str(i))
    if summ in dic:
        dic[summ] += 1
    else:
        dic[summ] = 1

maxx = float('-inf')
for i in dic:
    maxx = max(maxx, dic[i])
print(maxx)