z = 100 ** 2 + 625 ** 25 + 5 ** 100
st = ''

while z > 0:
    st += str(z % 15)
    z //= 15
st = st[::-1]
print(st.count('12'))