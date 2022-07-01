x = 0
st = ''

for i in range(1000000):
    x = i
    z = 125 ** 7 - 25 ** 4 + x
    st = ''
    while z > 0:
        st += str(z % 5)
        z //= 5
    st = st[::-1]
    if st.count('4') == 15 and st.count('3') == 1 and st.count('1') == 2:
        print(i)
        break