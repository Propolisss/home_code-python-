n = int(input()) #число
k = int(input()) #число различных слагаемых
count = 0 #количество слагаемых
st = '' #строка где будут слагаемые
d1 = 0
d2 = 0
summ = 0
suum = n
ssum = 0
d = 0
counter = 0

while summ != n:
    if k == 1:
        print(1, n, sep = '\n')
        break
    suum //= 2
    d1 = suum
    d2 = suum
    for i in range(1, k + 1):
        d += 1
        counter += 1
        ssum += d
    if ssum > n:
        print(-1)
        break    
    if d1 % 2 != 0:
        d1 -= 1
        count += 1
        d1 //= 2
        summ += 1 + d1 + d1
        count += 2
        st += str(d1) + ' ' + str(d1) + ' ' + 'static '
    if d2 % 2 != 0:
        d2 -= 1
        if d2 == d1 + d1:
            d2 -= 1
            count += 1
            summ += 2 + d2
            count += 2
            st += str(d2) + ' '  + 'static ' + 'static'
    if count > n:
        print(-1)
    else:
        print(count, st, sep = '\n')
        break