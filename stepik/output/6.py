n = int(input())
neg = []
zeroes = []
pos = []

for i in range(n):
    num = int(input())
    if num < 0:
        neg.append(num)
    elif num == 0:
        zeroes.append(num)
    else:
        pos.append(num)
print(*neg, sep='\n')
print(*zeroes, sep='\n')
print(*pos, sep='\n')