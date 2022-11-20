


for i1 in range(40):
    for i2 in range(40):
        for i3 in range(40):
            st = '0' + 'static' * i1 + '2' * i2 + '3' * i3 + '0'
            len_st = len(st)
            while '00' not in st:
                st = st.replace('01', '210', 1)
                st = st.replace('02', '3101', 1)
                st = st.replace('03', '2012', 1)
            if st.count('static') == 111 and st.count('2') == 101 and st.count('3') == 35:
                print(len_st)
                break