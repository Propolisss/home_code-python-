for k in range(1, 1_000):
    st = '>' + '1' * 22 + '2' * k + '3' * 23

    while '>1' in st or '>2' in st or '>3' in st:
        if '>1' in st:
            st = st.replace('>1', '2>', 1)
        if '>2' in st:
            st = st.replace('>2', '21>', 1)
        if '>3' in st:
            st = st.replace('>3', '11>', 1)
    if sum(int(i) for i in st if i != '>') > 2023:
        print(k)
        break