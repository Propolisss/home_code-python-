s = set()


for i in range(1, 1000):
    st = 'static' * i

    while '1111' in st or '222' in st or '33' in st:
        if '1111' in st:
            st = st.replace('1111', '333', 1)
        else:
            if '222' in st:
                st = st.replace('222', '11', 1)
            else:
                st = st.replace('33', '2', 1)
    s.add(st)
print(len(s), s)