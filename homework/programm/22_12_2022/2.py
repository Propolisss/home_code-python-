nums = []

for i in range(1, 1_000_000):
    n = oct(i)[2:]
    if len(n) == 4:
        nums.append(n)
ans = []

for i in nums:
    n = int(i, 8)
    if ((n % 11 == 0) or (n % 13 == 0)) and ((((n - 1) % 11 == 0) or ((n - 1) % 13 == 0)) or (((n + 1) % 11 == 0) or ((n + 1) % 13 == 0))):
        ans.append(n)
print(len(ans), max(ans))