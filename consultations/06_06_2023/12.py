for n in range(3, 100, 3):
    st = '1' * (n // 3) + '2' * (n // 3) + '3' * (n // 3)

    while '21' in st or '31' in st or '32' in st:
        if '21' in st:
            st = st.replace('21', '12', 1)
        if '31' in st:
            st = st.replace('31', '13', 1)
        if '32' in st:
            st = st.replace('32', '23', 1)
    if len(st) >= 50 and st[49] == '2':
        print(n)
        break