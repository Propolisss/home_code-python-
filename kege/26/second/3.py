file = open('26_936.txt')
n, s = map(int, file.readline().split())
nums = sorted(int(i) for i in file)
count = 0

while len(nums) > 0:
    temp = []
    if nums[-1] <= s:
        last = nums.pop(-1)
    for i in range(len(nums) - 1, -1, -1):
        if last + nums[i] <= s:
            last += nums[i]
            temp.append(i)
    for i in temp: nums.pop(i)

    count += 1
print(count, last)