with open('17.txt') as file:
    nums = [int(i) for i in file]

maxx = 0
for i in nums:
    if i % 10 == 3:
        maxx = max(maxx, i)

ans = []

for i in range(1, len(nums)):
    if (abs(nums[i - 1]) % 10 == 3 and abs(nums[i]) % 10 != 3) or (abs(nums[i - 1]) % 10 != 3 and abs(nums[i]) % 10 == 3):
        if ((nums[i - 1] ** 2) + (nums[i] ** 2)) >= (maxx ** 2):
            ans.append(nums[i - 1] ** 2 + nums[i] ** 2)
print(len(ans), max(ans))