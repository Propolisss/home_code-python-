list = input().split()
l = ''

for i in range(0, len(list)):
    if int(list[i]) % 2 == 0:
        l += str(list[i]) + ' '
print(l)