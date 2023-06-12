nums = [int(i) for i in open('17-343.txt')]
ans = []

def summ(n):
    summ1 = sum(int(n[i]) for i in range(len(n)) if i % 2 != 0)
    summ2 = sum(int(n[i]) for i in range(len(n)) if i % 2 == 0)
    if summ2 == 0:
        return summ1, float('inf')
    return summ1, summ2

for i in range(2, len(nums)):
    n1 = nums[i - 2]
    n2 = nums[i - 1]
    n3 = nums[i]
    if all(summ(str(i)[::-1])[0] % summ(str(i)[::-1])[1] == 0 for i in [n1, n2, n3]):
        ans.append(n1 + n2 + n3)
print(len(ans), min(ans))