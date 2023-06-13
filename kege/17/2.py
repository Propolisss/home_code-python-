nums = [int(i) for i in open('17_2013.txt')]
ans = []

for i in nums:
    if (i % 10 == 2 or i % 10 == 7) and i % 3 == 0 and i % 11 == 0:
        ans.append(i)
print(len(ans), min(ans))