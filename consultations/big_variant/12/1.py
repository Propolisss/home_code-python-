for n in range(6, 100_000):
    st = '2' + '4' * n
    while '14' in st or '244' in st or '444' in st:
        if '14' in st:
            st = st.replace('14', '2', 1)
        if '244' in st:
            st = st.replace('244', '14', 1)
        if '444' in st:
            st = st.replace('444', '21', 1)
    if sum(int(i) for i in st) > 20:
        print(n)
        break