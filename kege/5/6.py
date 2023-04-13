for i in range(1, 100 + 1):
    n = bin(i)[2:]
    n = str(int(n[::-1]))
    if int(n, 2) == 13:
        print(i)