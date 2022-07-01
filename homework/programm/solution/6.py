list = []

for i in range(1, 1000):
    st = '88' + '8' * i
    while ('555' in st) or ('888' in st):
        st = st.replace('555', '8', 1)
        st = st.replace('888', '55', 1)
    if st not in list:
        list.append(st)
print(len(list))