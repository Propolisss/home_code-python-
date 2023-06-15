file = open('26_2255.txt')
n, m = map(int, file.readline().split())
nums = [list(map(str, i.split())) for i in file]
for i in range(len(nums)):
    nums[i] = [int(nums[i][0]), nums[i][1]]
nums.sort()
summ = 0
count_a = 0
flags = [0] * n
mins = []
maxs = []
for i in range(len(nums)):
    if summ + nums[i][0] <= m:
        summ += nums[i][0]
        if nums[i][1] == 'A':
            count_a += 1
        else:
            maxs.append(nums[i][0])
        flags[i] = 1
    else:
        if nums[i][1] == 'A':
            mins.append(nums[i][0])

while summ - maxs[-1] + mins[0] <= m:
        summ += mins[0] - maxs[-1]
        mins.pop(0)
        del maxs[-1]
        count_a += 1
print(count_a, m - summ)