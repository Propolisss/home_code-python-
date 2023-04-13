st = '8' * 70

while '2222' in st or '8888' in st:
    if '2222' in st:
        st = st.replace('2222', '88', 1)
    else:
        st = st.replace('8888', '22', 1)
print(st)