st = '112' * 4 + '1' * 4

while '11' in st:
    if '112' in st:
        st = st.replace('112', '7', 1)
    else:
        st = st.replace('11', '3', 1)
print(sum(int(i) for i in st))