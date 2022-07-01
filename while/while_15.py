a = int(input())
f1 = 1
f2 = 1
k = 3

while f1 + f2 < a:
    k += 1
    f1, f2 = f2, f1 + f2
if f1 + f2 == a:
    print(k)
else:
    print(-1)