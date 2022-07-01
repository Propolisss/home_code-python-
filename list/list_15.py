N, K = [int(i) for i in input().split()]
list = ['I'] * N

for i in range(K):
    n, nn = [int(i) for i in input().split()]
    for j in range(n, nn + 1):
        list[j - 1] = '.'
print(''.join(list))