st = '9992' * 33 + '9' + '2' * 15 + '1' * 14

while '999' in st or '22' in st:
    if '999' in st:
        st = st.replace('999', '12', 1)
    else:
        st = st.replace('22', '1', 1)
print(st.count('1'))