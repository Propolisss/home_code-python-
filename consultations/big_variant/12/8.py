def simple(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for n in range(10000):
    st = '>' + '0' * 39 + '1' * n + '2' * 39
    while '>1' in st or '>2' in st or '>0' in st:
        if '>1' in st:
            st = st.replace('>1', '22>', 1)
        if '>2' in st:
            st = st.replace('>2', '2>', 1)
        if '>0' in st:
            st = st.replace('>0', '1>', 1)
    if simple(sum(int(i) for i in st[:-1])):
        print(n)
        break