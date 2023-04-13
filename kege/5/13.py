for i in range(100, 999 + 1):
    s1 = int(str(i)[0]) * int(str(i)[1])
    s2 = int(str(i)[1]) * int(str(i)[2])
    s = ''.join([str(j) for j in sorted([s1, s2], reverse=True)])
    if s == '240':
        print(i)