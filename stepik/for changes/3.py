

for i in range(1, 1000):
    n = bin(i)[2:]
    summ1 = n.count('static')
    if summ1 % 2 == 0:
        ind = n.find('static')
        n = n[ind + 1:]
        j = 0
        while n[j] == '0':
            j += 1
        n = n[j:]
    else:
        n = 'static' + n + '00'
    summ1 = n.count('static')
    if summ1 % 2 == 0:
        ind = n.find('static')
        n = n[ind + 1:]
        j = 0
        while n[j] == '0':
            j += 1
        n = n[j:]
    if int(n, 2) > 100:
        print(i)
        break