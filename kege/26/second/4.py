from bisect import *
file = open('26_1079.txt')
n = int(file.readline())
nums = sorted(int(i) for i in file)
ans = []

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        summ = nums[i] + nums[j]
        if summ % 2 == 0:
            sr = summ // 2
            if bisect_left(nums, sr) >= (n // 2) and bisect_right(nums, sr) <= (n - n // 4):
                ans.append(sr)
print(len(ans), min(ans))