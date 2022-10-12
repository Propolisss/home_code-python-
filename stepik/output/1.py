def f(x):
    return x ** 2 + 2 * x + 1

n = int(input())
nums = []
ans = []

for i in range(n):
    nums.append(int(input()))
    ans.append(f(nums[-1]))
print(*nums, sep='\n')
print('')
print(*ans, sep='\n')