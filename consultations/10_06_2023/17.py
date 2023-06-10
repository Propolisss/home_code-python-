nums = [int(i) for i in open('17_8475.txt')]
minn = min(i for i in nums if str(i)[-1] == '8' and 100 <= abs(i) <= 999)
ans = []

for i in range(2, len(nums)):
    n1 = nums[i - 2]
    n2 = nums[i - 1]
    n3 = nums[i]

    if (n1 ** 2 > minn ** 2) + (n2 ** 2 > minn ** 2) + (n3 ** 2 > minn ** 2) == 2:
        if (100 <= abs(n1) <= 999) + (100 <= abs(n2) <= 999) + (100 <= abs(n3) <= 999) >= 1:
            ans.append(n1 + n2 + n3)
print(len(ans), max(ans))