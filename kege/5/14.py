for i in range(100, 999 + 1):
    s1 = int(str(i)[0]) ** 2 + int(str(i)[1]) ** 2
    s2 = int(str(i)[1]) ** 2 + int(str(i)[2]) ** 2
    if ''.join([str(j) for j in sorted([s1, s2], reverse=True)]) == '9010':
        print(i)
        break