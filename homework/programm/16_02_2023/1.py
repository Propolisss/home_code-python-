file = open('26.txt')
n = int(file.readline())
nums = sorted(int(i) for i in file)
flags = [0] * len(nums)
count = 0
maxx = float('-inf')

for i in range(len(nums)):
    if not(flags[i]):
        flags[i] = 1
        temp_count = 1
        curr = nums[i]
        for j in range(i, len(nums)):
            if not (flags[j]) and abs((nums[j] - curr)) >= 7:
                temp_count += 1
                flags[j] = 1
                curr = nums[j]
        maxx = max(maxx, temp_count)
        count += 1
    else:
        continue
print(count, maxx)