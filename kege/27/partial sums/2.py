file = open('27-B_637.txt')
n = int(file.readline())
summ = [0]

for i in range(n):
    pair = list(map(int, file.readline().split()))
    summ = [a + b for a in pair for b in summ]
    summ = {x % 10 : x for x in sorted(summ)}.values()
print(max(i for i in summ if i % 10 != 5))