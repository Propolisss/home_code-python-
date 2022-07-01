n = int(input())
nums = [int(i) for i in input().split()]
nums.sort()

for i in range((len(nums) // 2) + 1):
    if nums[i] + nums[n - i - 2] != n + 1:
        if (n + 1) - nums[i] in nums:
            print(n + 1 - nums[n - i - 2])
            break
        else:
            print(n + 1 - nums[i])
            break