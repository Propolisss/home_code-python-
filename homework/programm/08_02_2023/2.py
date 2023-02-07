file = open('27-53b.txt')
n = int(file.readline())
nums = [int(i) for i in file]
nums.sort()
nn = 100
minn = float('inf')

for i in range(nn):
    for j in range(i + 1, nn):
        for k in range(j + 1, nn):
            if (nums[i] + nums[j] + nums[k]) % 3 == 0:
                minn = min(minn, nums[i] + nums[j] + nums[k])
                break
print(minn)