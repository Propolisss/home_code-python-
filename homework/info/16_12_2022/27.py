file = open('27A.txt')
n = int(file.readline())
buff = [int(file.readline()) for i in range(4)]
nums = [int(file.readline()) for _ in range(n - 4)]
k13_1 = 0
k13_0 = 0
k1 = 0
k0 = 0

count = 0

for i in range(len(nums)):
    if nums[i] % 13 == 0 and nums[i] % 2 == 0:
        count += k1
    elif nums[i] % 13 == 0 and nums[i] % 2 != 0:
        count += k0
    elif nums[i] % 2 == 0:
        count += k13_1
    else:
        count += k13_0

    curr_buff = buff[0]
    if curr_buff % 13 == 0 and curr_buff % 2 == 0: k13_0 += 1
    if curr_buff % 13 == 0 and curr_buff % 2 != 0: k13_1 += 1
    if curr_buff % 2 == 0: k0 += 1
    if curr_buff % 2 != 0: k1 += 1
    buff.append(nums[i])
    buff.pop(0)
print(count)