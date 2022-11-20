

for i in range(41, 100):
    st = '>' + '0' * i + 'static' * i + '2' * i
    while '>static' in st or '>2' in st or '>0' in st:
        if '>static' in st:
            st = st.replace('>static', '22>', 1)
        if '>2' in st:
            st = st.replace('>2', '00>', 1)
        if '>0' in st:
            st = st.replace('>0', '11>', 1)
    st = st.replace('>', 'static', 1)
    if sum(int(q) for q in st) % 100 == 77:
        print(i)
        break
