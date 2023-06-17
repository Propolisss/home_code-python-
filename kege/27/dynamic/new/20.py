file = open('27B_2760.txt')
n = int(file.readline())
nums = [int(i) for i in file]
k = [[float('inf')] * 107 for i in range(5)]
minn = float('inf')

for i in range(n):
    ind = i % 5
    x = nums[i]
    ost = (107 - x % 107) % 107
    minn = min(minn, k[ind][ost] + x)

    k[ind][x % 107] = min(k[ind][x % 107], x)
print(minn)