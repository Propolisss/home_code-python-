z = 7 ** 500 + 7 ** 200 - 7 ** 50
maxx = 0
summ = 0
st = ''

while z > 0:
    st += str(z % 7)
    z //= 7
st = st[::-1]

for i in range(1, len(st)):
    summ = 6 * i
    if summ > maxx:
        maxx = summ
print(maxx)