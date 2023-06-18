file = open('27-B_23.txt')
n = int(file.readline())
nums = [0]

for i in range(n):
    inner = list(map(int, file.readline().split()))
    summ = [a + b for a in inner for b in nums]
    nums = {x % 3 : x for x in sorted(summ)}.values()
print(max(i for i in nums if i % 3 != 0))