nums = []
size = 1000

for i in range(size ** 2):
    nums.append(i)

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    print(x * size + y)
