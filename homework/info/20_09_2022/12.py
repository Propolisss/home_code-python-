st = 'С' * 50 + 'Г' * 50 + 'Н' * 50

while 'ГС' in st or 'НС' in st or 'ГН' in st:
    if 'ГС' in st:
        st = st.replace('ГС', 'СГ', 1)
    if 'НС' in st:
        st = st.replace('НС', 'СН', 1)
    if 'ГН' in st:
        st = st.replace('ГН', 'НГ', 1)
print(st[10], st[90] + st[130])