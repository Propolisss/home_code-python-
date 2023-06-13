nums = [int(i) for i in open('17_2016.txt')]
ans = []

for i in nums:
    if i % 13 == 7 and i % 7 != 0 and i % 11 != 0:
        ans.append(i)
print(max(ans) - min(ans), len(ans))