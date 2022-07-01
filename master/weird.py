n = int(input())
ans = [n]

while n != 1:
    if n & 1:
        n = n * 3 + 1
        ans.append(n)
    else:
        n //= 2
        ans.append(n)

print(' '.join([str(i) for i in ans]))