file = open('26-93.txt')
n, m = map(int, file.readline().split())
dic = dict()
maxx_floor = float('-inf')

for i in file:
    nums = [int(j) for j in i.split()]
    if nums[0] in dic:
        dic[nums[0]][nums[1]] = 1
    else:
        dic[nums[0]] = [0] * 5001
        dic[nums[0]][nums[1]] = 1
    maxx_floor = max(maxx_floor, nums[0])

maxx_id = float('-inf')
count = 0

for i in range(maxx_floor + 1):
    if i in dic:
        if dic[i].count(1) < m:
            continue
        for j in range(len(dic[i])):
            if dic[i][j] == 0:
                summ = 0
                for k in range(j + 1, len(dic[i])):
                    if dic[i][k] == 1:
                        summ += 1
                    else:
                        break
                for k in range(j - 1, -1, -1):
                    if dic[i][k] == 1:
                        summ += 1
                    else:
                        break
                if summ >= m:
                    count += 1
                    maxx_id = max(maxx_id, i)
print(count, maxx_id)