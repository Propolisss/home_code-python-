summ = 0
last = 0
st = ''
N = 0

for i in range(1000):
    st = ''
    last = 0
    summ = 0
    N = i
    while N > 0:
        last = N % 2
        summ += last
        st += str(last)
        N //= 2
    st = st[::-1]
    st += str(summ % 2)
    summ += summ % 2
    st += str(summ % 2)
    summ += summ % 2
    if int(st, 2) > 85:
        print(i)
        break