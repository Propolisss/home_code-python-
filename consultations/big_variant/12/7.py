for n in range(6, 100_000):
    st = '1' + '5' * n + '2' + '5' * n
    while '15' in st or '255' in st or '555' in st:
        if '15' in st:
            st = st.replace('15', '2', 1)
        if '255' in st:
            st = st.replace('255', '1', 1)
        if '555' in st:
            st = st.replace('555', '12', 1)
    if 100 <= sum(int(i) for i in st) <= 999:
        print(n)