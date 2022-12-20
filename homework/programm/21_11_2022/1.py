def prod(n):
    prod_ = 1
    for i in str(n):
        prod_ *= int(i)
    return prod_

ans = []

for i in range(4616, 52311 + 1):
    if sum(int(j) for j in str(i)) == 10:
        if prod(i) == 0:
            ans.append(i)
print(len(ans), min(ans))