nums = [int(i) for i in open('17_2017.txt')]
ans = []

for i in nums:
    if i % 16 == 11 and i % 7 == 0 and i % 6 != 0 and i % 13 != 0 and i % 19 != 0:
        ans.append(i)
print(sum(ans), len(ans))