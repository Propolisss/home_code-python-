num = 9 ** 11 * 3 ** 20 - 3 ** 9 - 27

st = ''

while num:
    st += str(num % 3)
    num //= 3
print(st.count('2'))