maxx = 0

for i in range(1, 100 + 1):
    st = '3' * i
    while st.find('333') != -1:
        st = st.replace('333', '4', 1)
        st = st.replace('4444', '3', 1)
    if st == '43':
        maxx = i
print(maxx)