n = int(input())
nums = []
flag = 1

for i in range(2, n + 1, 2):
    nums.append(i)

for i in range(1, n + 1, 2):
    nums.append(i)

for i in range(1, len(nums)):
    if abs(nums[i - 1] - nums[i]) == 1:
        print('NO SOLUTION')
        flag *= 0
        break
    else:
        flag *= 1 

if flag:
    print(' '.join([str(i) for i in nums]))