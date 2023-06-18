file = open('27-B_2949.txt')
n = int(file.readline())
nums = [0] * 10

for i in range(n):
    x = int(file.readline())
    k = nums.copy()
    k[x % 10] += 1
    for j in range(10):
        k[(x + j) % 10] += nums[j]
    nums = k
print(nums[5])