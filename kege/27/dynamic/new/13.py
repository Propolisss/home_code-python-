file = open('27B_2761.txt')
n = int(file.readline())
nums = [int(i) for i in file]
ch = [0] * 13
nech = [0] * 13
count = 0
for i in range(5, n):
    x = nums[i]
    ost = nums[i] % 13
    if x % 2 == 0:
        count += nech[ost] + ch[ost]
    else:
        count += ch[ost]
    if nums[i - 5] % 2 == 0:
        ch[nums[i - 5] % 13] += 1
    else:
        nech[nums[i - 5] % 13] += 1
print(count)