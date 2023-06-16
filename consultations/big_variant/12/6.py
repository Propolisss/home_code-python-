st = '>' + '1' * 15 + '2' * 20 + '3' * 25

while '>1' in st or '>2' in st or '>3' in st:
    if '>1' in st:
        st = st.replace('>1', '22>', 1)
    if '>2' in st:
        st = st.replace('>2', '2>1', 1)
    if '>3' in st:
        st = st.replace('>3', '1>', 1)
print(sum(int(i) for i in st[:-1]))