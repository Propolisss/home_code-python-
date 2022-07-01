a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if ((abs(a1 - a2) == 0 or abs(a1 - a2) == 1) and (abs(b1 - b2) == 0 or abs(b1 - b2) == 1)):
    print('yes')
else:
    print('no')