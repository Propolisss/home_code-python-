file = open('26_2612.txt')
n, m = map(int, file.readline().split())
nums = sorted(int(i) for i in file)
no = []
ans = dict()
minn = float('inf')
temp = m

for i in range(n - 1, -1, -1):
    if m != 0:
        m -= 1
        if nums[i] in ans:
            ans[nums[i]] += 1
        else:
            ans[nums[i]] = 1
    elif nums[i] in ans:
        ans[nums[i]] += 1
    else:
        no.append(nums[i])

for i in range(300, -1, -1):
    if i in ans:
        if temp - ans[i] >= 0:
            temp -= ans[i]
            minn = min(minn, i)
print(minn, sum(no) // len(no))