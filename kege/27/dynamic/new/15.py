file = open('27B_2754.txt')
n = int(file.readline())
nums = [int(i) for i in file]
mx = [float('-inf')] * 137
mn = [float('inf')] * 137
maxx = float('-inf')

for i in range(4, n):
    x = nums[i]
    ost = x % 137
    if mn[ost] != float('inf') and mx[ost] != float('-inf'):
        maxx = max(maxx, abs(x - mn[ost]), abs(x - mx[ost]))
    if mn[ost] != float('inf'):
        maxx = max(maxx, abs(x - mn[ost]))
    elif mx[ost] != float('-inf'):
        maxx = max(maxx, abs(x - mx[ost]))

    mx[nums[i - 4] % 137] = max(mx[nums[i - 4] % 137], nums[i - 4])
    mn[nums[i - 4] % 137] = min(mn[nums[i - 4] % 137], nums[i - 4])
print(maxx)