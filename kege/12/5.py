for i in range(1, 50 + 1):
    st = '6' * i

    while '66' in st:
        st = st.replace('66', '1', 1)
        st = st.replace('11', '2', 1)
        st = st.replace('22', '6', 1)
    if st == '21':
        print(i)