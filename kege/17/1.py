nums = [int(i) for i in open('17_2003.txt')]
ans = []

for i in nums:
    if i % 3 == 0 and i % 7 != 0 and i % 17 != 0 and i % 19 != 0 and \
        i % 27 != 0:
        ans.append(i)
print(len(ans), max(ans))