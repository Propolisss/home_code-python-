def div(n):
    dels_ = set()

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            dels_ |= {i, n // i}
    return dels_

for m in range(1000):
    st = '>' + '1' * 17 + '2' * 34 + '3' * m
    while '>1' in st or '>2' in st or '>3' in st:
        if '>1' in st:
            st = st.replace('>1', '22>')
        if '>2' in st:
            st = st.replace('>2', '2>')
        if '>3' in st:
            st = st.replace('>3', '1>')
    if len(div(sum(int(i) for i in st if i.isdigit()))) == 3:
        print(m)