ans = []

for i in range(1, 30):
    n = bin(i)[2:]
    if n.count('1') % 2 == 0:
        n = '10' + n[:-2] + '00'
    else:
        n = '11' + n[:-2] + '11'
    ans.append(int(n, 2))
print(max(ans))