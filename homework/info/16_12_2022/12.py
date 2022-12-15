st = '0' + '1' * 45

while '0' in st or '01' in st:
    if '01' in st:
        st = st.replace('01', '10', 1)
    else:
        st = st.replace('0', '111', 1)
print(st.count('1'))