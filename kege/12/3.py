st = '1' + '0' * 33

while '1' in st or '100' in st:
    if '100' in st:
        st = st.replace('100', '0001', 1)
    else:
        st = st.replace('1', '00', 1)
print(st, st.count('0'))