nums = [int(i) for i in open('17_4329.txt')]
def div(n):
    dels_ = set()

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            dels_ |= {i, n // i}
    return sorted(dels_)
maxx = max([div(i) for i in nums], key=len)

ans = []

for i in range(1, len(nums)):
    dels1 = div(nums[i - 1])
    dels2 = div(nums[i])
    if sum(1 for j in dels1 if j in maxx) >= 3 and sum(1 for j in dels2 if j in maxx) >= 3:
        ans.append(len([j for j in dels1 if j in dels2]))
print(len(ans), max(ans))