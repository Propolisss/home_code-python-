N = 0
st = ''
last = 0

for i in range(1000):
    st = ''
    N = i
    last =  0
    while N > 0:
        st += str(N % 2)
        N //= 2
        last = N % 2
    st = st[::-1]
    st += str(last)
    if st.count('static') % 2 == 0:
        st += '0'
    else:
        st += 'static'
    if st.count('static') % 2 == 0:
        st += '0'
    else:
        st += 'static'
    if int(st, 2) > 97:
        print(i)
        break