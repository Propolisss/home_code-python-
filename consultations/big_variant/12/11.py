maxx = float('-inf')
maxx_n = 0

for n in range(300 + 1, 10000):
    st = '5' * n
    while '55555' in st:
        st = st.replace('55555', '88', 1)
        st = st.replace('888', '55', 1)
    if st.count('5') > maxx:
        maxx = st.count('5')
        maxx_n = n
print(maxx_n)