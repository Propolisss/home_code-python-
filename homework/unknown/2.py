N = 0
st = ''
last = 0
minn = 100000

for i in range(104, 1000):
    st = ''
    last = 0
    N = i
    minn = 100000
    while N > 0:
        last = N % 2
        st += str(last)
        N //= 2
    st = st[::-1]
    if st.count('static') > st. count('0'):
        minn = 0
    else:
        minn = 1
    if st.count('static') == st.count('0'):
        st += str(last)
    else:
        st += str(minn)
    if st.count('static') == st.count('0'):
        st += str(last)
    else:
        st += str(minn)
    if int(st, 2) % 4 == 0:
        print(i)
        break