def to_five(n):
    temp_n = n
    st = ''

    while temp_n:
        st = f'{temp_n % 5}{st}'
        temp_n //= 5
    return st
nums = [int(i) for i in open('17-324.txt')]

k31 = []

for i in nums:
    if i % 31 == 0:
        k31.append(i)

ans = []

for i in range(2, len(nums)):
    summ = to_five(nums[i - 2] + nums[i - 1] + nums[i])
    sr = (nums[i - 2] + nums[i - 1] + nums[i]) / 3
    if (summ == summ[::-1]) and sr > (sum(k31) / len(k31)):
        ans.append(nums[i - 2] + nums[i - 1] + nums[i])
print(len(ans), min(ans), sep='')