n = int(input()) #число
k = int(input()) #число различных слагаемых
count = 0 #количество слагаемых
st = '' #строка где будут слагаемые
d = 0
dd = 0
counter = 0

for i in range(1, n + 1):
    st = ''
    suum = n
    summ = n
    count = 0
    counter = 0
    dd = 0
    if k > 2:
        d = n - k
        summ -= d
    else:
        d = n - (k - 1)
        summ -= d
    while summ >= 0:
        st += str(d) + ' '
        summ -= 1
        d = summ
        counter += 1
    if counter == k:
        print(counter, st, end = '', sep = '\n')
        break