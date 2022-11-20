file = open('27A.txt')
n = int(file.readline())
nums = [int(i) for i in file]
dic = dict()

for i in nums:
    for j in range(len(str(i))):
        if str(i)[j] in dic:
            dic[str(i)[j]] += 1
        else:
            dic[str(i)[j]] = 1
minn = float('inf')

for i in dic:
    minn = min(minn, dic[i])
print(minn)