file = open('26-89.txt')
n = int(file.readline())
nums = sorted([int(i) for i in file])
ans = dict()

for i in range(len(nums)):
    last = nums[i]
    count = 1
    for j in range(i + 1, len(nums)):
        if nums[j] - last >= 3:
            last = nums[j]
            count += 1
    if count in ans:
        ans[count].add(nums[i])
    else:
        ans[count] = {nums[i]}
print(max(ans), ans[max(ans)])