file = open('27-B_814.txt')
n = int(file.readline())
summ = [0]

for i in range(n):
    pair = list(map(int, file.readline().split()))
    summ = [a + b for a in pair for b in summ]
    summ = {x % 5 : x for x in sorted(summ, reverse=1)}.values()
print(min(i for i in summ if i % 5 != 0))