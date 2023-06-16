file = open('26_1257.txt')
n = int(file.readline())
nums = [int(i) for i in file]
set_nums = set(nums)
ans = []

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if (nums[i] + nums[j]) in set_nums and nums[i] % 2 != nums[j] % 2:
            ans.append(nums[i] + nums[j])
print(len(ans), max(ans))