n1 = -1
k = 0
max_k = 0
n2 = int(input())

while n2 != 0:
    if n1 == n2:
        k += 1
    else:
        n1 = n2
        max_k = max(max_k, k)
        k = 1
    n2 = int(input())
max_k = max(max_k, k)

print(max_k)