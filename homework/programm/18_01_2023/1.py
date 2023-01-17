nums = [int(i) for i in open('17-2.txt')]

minn = min(nums)
ans = []

for i in range(len(nums)):
    if nums[i] == minn:
        ans.append(i + 1)
print(len(ans), ans[-1])