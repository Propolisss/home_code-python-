file = open('27A_4116.txt')
n, k = map(int, file.readline().split())
nums = [int(i) for i in file]
st, end = 0, 0
summ = nums[0]

while nums[end + 1] + summ <= k:
    end += 1
    summ += nums[end]
maxx = end - st + 1

for i in range(1, n):
    summ -= nums[i - 1]
    st += 1
    while end + 1 < n and nums[end + 1] + summ <= k:
        end += 1
        summ += nums[end]
    maxx = max(maxx, end - st + 1)
print(maxx)