file = open('26_2617.txt')
n = int(file.readline())
nums = sorted(int(i) for i in file)
razn = [0] + [nums[i + 1] - nums[i] for i in range(n - 1)]
k = int(n * 0.2)
for i in range(n - k, -1, -1):
    if razn[i] > max(razn[:i]):
        print(len(nums[i:]), nums[i])
        break