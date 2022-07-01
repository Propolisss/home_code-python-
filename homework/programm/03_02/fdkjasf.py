summ = 0
z = 7 ** 500 + 7 ** 200 - 7 ** 50
st = ''

while z > 0:
    st += str(z % 7)
    summ += z % 7
    z //= 7
st = st[::-1]
print(len(st), summ)
print(st)