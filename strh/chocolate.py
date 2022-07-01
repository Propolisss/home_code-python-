a = int(input())
b = int(input())
c = int(input())

if (c % a == 0 or c % b == 0) and (a * b) > c:
    print('yes')
else:
    print('no')