count = 0

for n in range(1, 100 + 1):
    st = '1' + '0' * n
    while '01' in st or '1' in st:
        if '10' in st:
            st = st.replace('10', '0001', 1)
        else:
            if '1' in st:
                st = st.replace('1', '0', 1)
    if len(st) % 7 == 0:
        count += 1
print(count)