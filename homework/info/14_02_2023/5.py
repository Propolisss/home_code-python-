for i in range(1, 128 + 1):
    n = '0' * (8 - len(bin(i)[2:])) + bin(i)[2:]
    n = n.replace('1', '2').replace('0', '1').replace('2', '0')
    if int(n, 2) + 1 == 153:
        print(i)