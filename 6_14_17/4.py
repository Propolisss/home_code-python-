z = 81 ** 18 - (81 ** 8 - 1) * ((8 + 1) ** 8 + 1) // 8 - 8
st = ''

while z > 0:
    st += str(int(z) % 3)
    z //= 3
print(st.count('1'))