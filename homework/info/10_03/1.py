maxx = 0

for i in range(1000):
    N = i
    num = hex(i // 2)
    num = num[2:]
    if N % 4 != 0:
        num = 'F' + num + 'A0'
    else:
        num = '15' + num + 'C'
    if int(num, 16) < 65636:
        if i > maxx:
            maxx = i
print(maxx)