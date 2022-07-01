a = int(input())
b = int(input())

for i in range(a, b + 1):
    st = str(i)
    if st[:2] == st[-1:-3:-1]:
        print(i)