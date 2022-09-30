with open('17-4.txt') as file:
    nums = [int(i) for i in file]

ans = []

for i in range(len(nums)):
    if ((nums[i] % 10 == 2) or (nums[i] % 10 == 7)) and (nums[i] % 3 == 0 and nums[i] % 11 == 0):
        ans.append(nums[i])
print(len(ans), min(ans))