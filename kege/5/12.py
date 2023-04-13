for i in range(1000, 9999 + 1):
    s1 = int(str(i)[0]) * int(str(i)[1])
    s2 = int(str(i)[2]) * int(str(i)[3])
    arr = sorted([s1, s2])
    s = ''.join(str(j) for j in arr)
    if s == '1214':
        print(i)