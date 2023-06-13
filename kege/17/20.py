nums = [int(i) for i in open('17_2399.txt')]
summ = sum(int(i) for x in nums for i in str(x) if x % 35 == 0)
ans = []

for i in range(1, len(nums)):
    if (nums[i - 1] > summ and nums[i] <= summ and hex(nums[i])[-2:] == 'ef') or (nums[i] > summ and nums[i - 1] <= summ and hex(nums[i - 1])[-2:] == 'ef'):
        ans.append(nums[i - 1] + nums[i])
print(len(ans), min(ans))