import math
x, y = input().split()
r = int(input())

if math.sqrt(int(x) ** 2 + int(y) ** 2) <= r:
    print('Победа!')
else:
    print('Надеюсь, это была не последняя попытка')