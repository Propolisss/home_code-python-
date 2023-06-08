count = 0

for i in range(1000, 9999 + 1):
    if i // 1000 % 2 == 0:
        r = int(str(i)[0]) + int(str(i)[-2]) + ( abs( int(str(i)[1]) - int(str(i)[3])) )
    else:
        temp = ''.join(sorted(str(i)))
        r = bin(int(temp))[2:].count('1')
    if r > 20:
        count += 1
print(count)