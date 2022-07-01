z = 81**15 + 3**22 - 27
st = ''

while z > 0:
    st += str(z % 9)
    z //= 9
print(st.count('8'))