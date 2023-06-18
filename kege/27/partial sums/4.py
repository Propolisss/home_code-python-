file = open('27B_682.txt')
n = int(file.readline())
summ = [0]

for i in range(n):
    trio = list(map(int, file.readline().split()))
    nums = [trio[0] + trio[1], trio[0] + trio[2], trio[1] + trio[2]]
    summ = [a + b for a in nums for b in summ]
    summ = {x % 4 : x for x in sorted(summ)}.values()
print(max(i for i in summ if i % 4 == 0))