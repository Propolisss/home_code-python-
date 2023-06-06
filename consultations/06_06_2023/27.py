file = open('27-126b.txt')
n = int(file.readline())
nums = [list(map(int, i.split())) for i in file]
maxx = float('-inf')

for i in range(n):
    for j in range(i + 1, n):
        if nums[j][1] > nums[i][1]:
            maxx = max(maxx, j - i)
        if nums[j][1] > nums[i][1]:
            break
print(maxx)