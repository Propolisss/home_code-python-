def to_base(n, base):
    temp_n = n
    st = ''

    while temp_n:
        st = str(temp_n % base) + st
        temp_n //= base
    return st


nums = [int(i) for i in open('17 (4).txt')]
maxx = float('-inf')

for i in nums:
    if i % 107 == 0:
        maxx = max(maxx, i)

ans = []

for i in range(1, len(nums)):
    if (nums[i - 1] > maxx or nums[i] > maxx) and ('36' in to_base(nums[i - 1], 7) or '36' in to_base(nums[i], 7)):
        ans.append(nums[i - 1] + nums[i])
print(len(ans), min(ans))