st = '010'

while '00' not in st:
    st = st.replace('01', '210', 1)
    st = st.replace('02', '3101', 1)
    st = st.replace('03', '2012', 1)
print(st)