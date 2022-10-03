n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
minn = 10 ** 10

if (n1 < minn):
    minn = n1
if n1 < minn:
    minn = n2
if n3 < minn:
    minn = n3
if n4 < minn:
    minn = n4
print(minn)