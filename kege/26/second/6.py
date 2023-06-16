file = open('26_2652.txt')
n = int(file.readline())
dic = dict()
nums = [int(i) for i in file]

for i in nums:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
print(len(dic), max(dic.values()))