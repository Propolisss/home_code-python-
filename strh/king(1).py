a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if (a1 - a2 == 0 or a1 - a2 == 1) and (b1 - b2 == 0 or b1 - b2 == 1):
    print('yes')
elif (a1 - a2) * (-1) == 1:
    print('yes')
elif (b1 - b2) * (-1) == 1:
    print('yes')
else:
    print('no')