st = '1' * 46 + '2' * 31

while '1111' in st:
    st = st.replace('1111', '2', 1)
    st = st.replace('222', '1')
print(st)