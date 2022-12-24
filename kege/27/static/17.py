file = open('27A.txt')
n = int(file.readline())
nums = [int(i) for i in file]
dic = dict()

for i in nums:
    if str(i)[0] in dic:
        dic[str(i)[0]] += 1
    else:
        dic[str(i)[0]] = 1


minn = float('inf')
minn_let = ''

for i in dic:
    if dic[i] < minn:
        minn = dic[i]
        minn_let = i

count = 0
for i in nums:
    if str(i)[0] == minn_let:
        count += 1
print(count)