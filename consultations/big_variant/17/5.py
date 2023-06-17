nums = [int(i) for i in open('17_7716.txt')]
maxx = max(i for i in nums if all(let in '13579' for let in str(i)))
ans = []

for i in range(1, len(nums)):
    if (all(let in '02468' for let in str(nums[i - 1])) or (all(let in '02468' for let in str(nums[i])))) and nums[i - 1] + nums[i] > maxx:
        ans.append(nums[i - 1] + nums[i])
print(len(ans), max(ans))