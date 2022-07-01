st = 'AB' * 52

while ('AA' in st) or ('BB' in st) or ('AB' in st):
    st = st.replace('AA', 'B', 1)
    st = st.replace('BB', 'A', 1)
    st = st.replace('AB', 'BA', 1)
print(st)