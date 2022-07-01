list = input().split()
l = ''

for i in range(1, len(list)):
    if int(list[i]) > int(list[i - 1]):
        l += str(list[i]) + ' '
print(l)