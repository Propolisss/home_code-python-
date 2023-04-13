st = '03'

while '01' in st or '02' in st or '03' in st:
    st = st.replace('01', '302', 1)
    st = st.replace('02', '3103', 1)
    st = st.replace('03', '20', 1)
print(st)