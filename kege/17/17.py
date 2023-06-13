nums = [int(i) for i in open('17_2310.txt')]
n = [i for i in nums if str(i)[-1] == '4']
summ = max(n) + min(n)
ans = []

for i in range(1, len(nums)):
    if (nums[i - 1] + nums[i]) < summ:
        ans.append(nums[i - 1] + nums[i])
print(len(ans), max(ans))