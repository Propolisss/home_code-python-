ch = input().split()
ss = list(int(i) for i in ch)

for i in range(len(ss)):
    for j in range(len(ss)):
        if i != j and ss[i] == ss[j]:
            break
    else:
        print(ss[i])