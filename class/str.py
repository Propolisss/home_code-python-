a = input()
b = input()
c = input()

if (abs(len(a) - len(b)) == abs(len(a) - len(c))) or (abs(len(a) - len(b)) == abs(len(b) - len(c))):
    print('YES')
else:
    print('NO')