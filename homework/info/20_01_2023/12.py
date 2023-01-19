st = '7' * 61

while '777' in st or '73' in st:
    if '777' in st:
        st = st.replace('777', '73', 1)
    else:
        st = st.replace('73', '7', 1)
print(st)