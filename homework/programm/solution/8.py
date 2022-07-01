st = '3' + '6' * 115 + '3'

while ('63' in st) or ('664' in st) or  ('6665' in st):
    if ('63' in st):
        st = st.replace('63', '4', 1)
    else:
        if ('664' in st):
            st = st.replace('664', '65', 1)
        else:
            if ('6665' in st):
                st = st.replace('6665',  '63', 1)
print(st)