st = '2' + '5' * 81

while '25' in st or '355' in st or '4555' in st:
    if '25' in st:
        st = st.replace('25', '4', 1)
    if '355' in st:
        st = st.replace('355', '2', 1)
    if '4555' in st:
        st = st.replace('4555', '3', 1)
print(st)