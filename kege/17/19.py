nums = [int(i) for i in open('17_2398.txt')]

def f(n):
    return n > 0 and str(n)[-1] == '9'

ans = []

for i in range(2, len(nums)):
    if not(f(nums[i - 2])) and f(nums[i - 1]) and not(f(nums[i])):
        ans.append(nums[i - 2] + nums[i - 1] + nums[i])
print(len(ans), max(ans))