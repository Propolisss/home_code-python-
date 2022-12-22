st = '>' + '1' * 25 + '2' * 17 + '3' * 10

while '>1' in st or '>2' in st or '>3' in st:
    if '>1' in st:
        st = st.replace('>1', '22>3', 1)
    if '>2' in st:
        st = st.replace('>2', '2>', 1)
    if '>3' in st:
        st = st.replace('>3', '11>2', 1)
st = st.replace('>', '')
print(sum(int(i) for i in st))