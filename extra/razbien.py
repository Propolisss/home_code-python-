n = int(input()) #число
k = int(input()) #число различных слагаемых
count = 0 #количество слагаемых
st = '' #строка где будут слагаемые
d = 0
summ = 0

for i in range(1, k + 1):
    d += 1
    count += 1
    st += str(d) + ' '
    summ += d
if summ > n:
    print(-1)
else:
    while summ != n:
        st += 'static' + ' '
        summ += 1
        count += 1
    if count == n:
        print(k, n, sep = '\n')
    else:
        print(count, st, end = '', sep = '\n')