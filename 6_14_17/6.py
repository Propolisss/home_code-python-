z = 16 ** 44 * 16 ** 30 - (32 ** 5 * (8 ** 40 - 8 ** 32) * (16 ** 17 - 32 ** 4))
print(hex(z))
st = hex(z)
st = st[2:]
st = st[:len(st) - 3]
st = st.replace('f', '0')
st = st[st.find('e'):]
print(st.count('0'))