from time import time
time_ = time()
start = time_

file = open('27b_8491.txt')
n = int(file.readline())
k = int(file.readline())
m = int(file.readline())
nums = [int(i) for i in file] + [0] * (k + 10000)
maxx_num1 = float('-inf')
maxx_num2 = float('-inf')
maxx_summ = float('-inf')

for i in range(len(nums)):
    if i % 1000 == 0:
        print(i, n - (k * (m - 1) + i), time() - time_, maxx_summ)
        time_ = time()
    if k * (m - 1) + i >= n:
        break
    curr_summ = 0
    #print(max(nums[:i + 1]), end=' ')
    for j in range(1, m - 1):
        curr_summ += nums[k * j + i]
        #print(nums[k * j + i], end=' ')
    #print(max(nums[k * (m - 1) + i:]))
    maxx_num1 = max(maxx_num1, nums[i])
    curr_summ += maxx_num1
    curr_summ += max(nums[k * (m - 1) + i:])
    maxx_summ = max(maxx_summ, curr_summ)
print(maxx_summ, time() - start)