z = 2 ** 51 + 2 ** 40 + 2 ** 35 + 2 ** 17 - 2 ** 5
st = hex(z)
st = st[2:]
list = []

for i in range(len(st)):
    if st[i] not in list:
        list.append(st[i])
print(len(list))