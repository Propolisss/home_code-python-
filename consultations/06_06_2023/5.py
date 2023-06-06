count = 0

for i in range(1000, 9999 + 1):
    r = str(i)
    if int(str(i)[0]) % 4 == 0:
        r = '9' + str(i)[1:]
    elif int(str(i)[0]) % 2 == 0:
        r = '3' + str(i)[1:]
    if r[0] == '9' and int(r) % 8 == 4:
        count += 1
print(count)